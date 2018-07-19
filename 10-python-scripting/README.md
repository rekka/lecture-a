# Scripting with Python.

Python has a very extensive library for working with files, running
external commands or parsing command line arguments. It is a pretty
great language for general scripting.

## Today's goal

Write a python script `build.py` that will look for all `*.c` and `*.cpp` files in
the subdirectory `./src` and compile them into a directory `./bin`. It
should preserve directory structure.

- By default, it should compile them without optimizations into `./bin/debug`.
If a command line flag `-O` is provided, it should compile them with
optimizations enabled (`-O3`) and save them in `./bin/release`.

    ```
    $ tree                                                                         master *=
    .
    ├── build
    │   ├── debug
    │   │   ├── app
    │   │   └── numbers
    │   │       ├── one
    │   │       └── two
    │   └── release
    │       ├── app
    │       └── numbers
    │           ├── one
    │           └── two
    ├── build.py
    └── src
        ├── app.c
        └── numbers
            ├── one.c
            └── two.c
    ```

- To save time, it should recompile only the files that have changed by
  comparing the modification date of the source file and the target
  binary.

## Running external commands: module `subprocess`

Allows you to run external commands, provide standard input and capture
standard output and return code.

**Example.** Get information about the system by running the system
 command `uname -a`.

```python
>>> import subprocess
>>> subprocess.run(['uname', '-a'])
Darwin bertik-mbp.local 17.6.0 Darwin Kernel Version 17.6.0: Tue May  8 15:22:16 PDT 2018; root:xnu-4570.61.1~1/RELEASE_X86_64 x86_64
CompletedProcess(args=['uname', '-a'], returncode=0)
```

To capture the command's output instead of printing it out to the
screen, use argument `stdout=subprocess.PIPE`.

```python
>>> result = subprocess.run(['uname', '-a'], stdout=subprocess.PIPE)
>>> result.stdout
b'Darwin bertik-mbp.local 17.6.0 Darwin Kernel Version 17.6.0: Tue May  8 15:22:16 PDT 2018; root:xnu-4570.61.1~1/RELEASE_X86_64 x86_64\n'
```

Errors can be tested for as well.

```python
>>> result = subprocess.run(['rm'], stdout=subprocess.PIPE)
usage: rm [-f | -i] [-dPRrvW] file ...
       unlink file
>>> result.returncode
64
```

But the error message was printed to screen. This is because errors are
printed by convention to `stderr`, not `stdout`. To capture the error
message, add `stderr=subprocess.PIPE`.

```python
>>> result = subprocess.run(['rm'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> result.stderr
b'usage: rm [-f | -i] [-dPRrvW] file ...\n       unlink file\n'
```

**Exercise.** Use `subprocess.run` to compile a C file without or with
optimizations enabled. If a compiler error is detected, print a nice
error message.

## Working with paths: module `pathlib`

_Note._ Requires Python >=3.4.

Module `pathlib` provides a class `Path` for working with system paths.

```python
>>> from pathlib import Path
>>> src = Path('src')
>>> src.is_file()
False
>>> src.is_dir()
True
>>> src
PosixPath('src')
>>> src / 'app.c'
PosixPath('src/app.c')
>>> (src / 'app.c').is_file()
True
```

It is easy to extract parts of the file name.

```python
>>> file = src / 'app.c'
>>> file
PosixPath('src/app.c')
>>> file.stem
'app'
>>> file.suffix
'.c'
>>> file.parent
PosixPath('src')
>>> file.relative_to(src)
PosixPath('app.c')
```

Listing all files matching given pattern in a given directory and its
subdirectories (recursively) can be done using `rglob`.

```python
>>> list(src.rglob('*.c'))
[PosixPath('src/app.c'), PosixPath('src/numbers/two.c'), PosixPath('src/numbers/one.c')]
```

Note that `rglob` returns a generator so it can be iterated over
directly. This is why we need to use `list` to get a list above.

```python
>>> for f in src.rglob('*.c'):
...     print(f)
...
src/app.c
src/numbers/two.c
src/numbers/one.c
```

We can get the relative paths.

```python
>>> for f in src.rglob('*.c'):
...     print(f.relative_to(src))
...
app.c
numbers/two.c
numbers/one.c
```

**Exercise.**

- Print the number of all files in the directory `/tmp`.

- Print the number of all subdirectories in the directory `/tmp`.


### Creating directories

A directory can be created by `mkdir`. By default, the parent
directories must exist. If you want to create the parent directories as
well, use `parents=True`.

```python
>>> dir = Path('test_dir/my/test')
>>> dir.mkdir()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/bertik/anaconda3/lib/python3.6/pathlib.py", line 1226, in mkdir
    self._accessor.mkdir(self, mode)
  File "/Users/bertik/anaconda3/lib/python3.6/pathlib.py", line 387, in wrapped
    return strfunc(str(pathobj), *args)
FileNotFoundError: [Errno 2] No such file or directory: 'test_dir/my/test'
>>> dir.mkdir(parents=True)
```

If the directory already exists, an error is produced.

```python
>>> dir.mkdir(parents=True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/bertik/anaconda3/lib/python3.6/pathlib.py", line 1226, in mkdir
    self._accessor.mkdir(self, mode)
  File "/Users/bertik/anaconda3/lib/python3.6/pathlib.py", line 387, in wrapped
    return strfunc(str(pathobj), *args)
FileExistsError: [Errno 17] File exists: 'test_dir/my/test'
```

Check for its existence first.

```python
>>> if not dir.exists():
...     dir.mkdir(parents=True)
...
```

**Exercise.**

- For all `*.c` files in directory `./src`, create an appropriate
    directory in `./build/debug`.

    _Hint._ Use `rglob()`, `relative_to()`, `parent`, `mkdir(parents=True)`.

- Compile each `*.c` file using `gcc` to a binary located in
  `./build/debug`.

    _Example._ `./src/app.c` should be compiled to `./build/debug/app`.

    _Hint._ Remove suffix by `.with_suffix('')`. Convert a `Path` `f` to
    string using `str(f)`.


## Parsing command line arguments: module `argparse`

We want fancy command line argument parsing and checking for our script. This is
where the module `argparse` comes in.

For more information see [the official
tutorial](https://docs.python.org/3/howto/argparse.html).

We need for now one optional command line argument `-O`. If present, it
will enable optimizations. Save the following in `build.py`.

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-O', action='store_true',
                    help='enable optimizations')
args = parser.parse_args()

if args.O:
    print('Optimizations enabled')
else:
    print('Optimizations disabled')
```

Now we can run the script with command line arguments.

```bash
$ python build.py                                                              master *=
Optimizations disabled
$ python build.py -O                                                           master *=
Optimizations enabled
```

`argparse` provides nice error messages and help.

```bash
$ python build.py -o                                                           master *=
usage: build.py [-h] [-O]
build.py: error: unrecognized arguments: -o
$ python build.py -h                                                           master *=
usage: build.py [-h] [-O]

optional arguments:
  -h, --help  show this help message and exit
  -O          enable optimizations
```

**Exercise.**

- Compile all `*.c` files in the `./src` directory as before, but based
  on the presence of the `-O` flag, compile them with or without
  optimizations into the directory `./build/release` or `./build/debug`.

## Checking modification time

`Path` objects have `stat()` function that returns information about a
file.

```python
>>> file = src / 'app.c'
>>> file.stat()
os.stat_result(st_mode=33188, st_ino=8604286092, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=59, st_atime=1531959253, st_mtime=1531959277, st_ctime=1531959277)
```

`st_mtime` contains the last modification time.


```
>>> file.stat().st_mtime
1531959277.5515637
```


**Exercise.**

- Compile the given `*.c` file only if it was modified after it was
  compiled before.

    _Hint._ Compare the last modification times of the file and its
    resulting binary (only if it already exists!).

- Compile also `*.cpp` files using `g++` in the same way.

- Stop the compilation when `gcc` or `g++` produce an error and print
  the error message.

- _Bonus._ Print an error if `*.cpp` and `*.c` compile to the binary with
  the same name.

    _Example._ `src/app.c` and `src/app.cpp` compile to the same
    `build/debug/app`. The user should be warned when this happens :)
