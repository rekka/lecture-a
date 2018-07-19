import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-O', action='store_true',
                    help='enable optimizations')
args = parser.parse_args()

if args.O:
    print('Optimizations enabled')
else:
    print('Optimizations disabled')
