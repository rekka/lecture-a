import argparse
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-O', action='store_true',
                    help='enable optimizations')
args = parser.parse_args()

src = Path('src')
if args.O:
    build = Path('build/release')
    gcc_args = ['-O3']
else:
    build = Path('build/debug')
    gcc_args = []

for f in src.rglob('*.c'):
    dest = (build / f.relative_to(src)).with_suffix('')
    if dest.exists():
        if dest.stat().st_mtime >= f.stat().st_mtime:
            print("Skipping {}".format(f))
            continue

    if not dest.parent.exists():
        dest.parent.mkdir(parents=True)

    print("Building {}...".format(f))
    subprocess.run(['gcc', str(f), '-o', str(dest)] + gcc_args)
