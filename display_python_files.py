import os
import sys

# Prints the given file with line numbers 
def print_file(filename):
    with open(filename) as f:
        print("\n\n" + filename)
        print('-' * len(filename))
        for (lineno, line) in enumerate(f, start=1):
            print(f"{lineno:03}: {line}", end='')

# if command line argumennt is given then use it else current directory 
if len(sys.argv) > 1:
    root = sys.argv[1]
else:
    root = r"."

allfiles = os.walk(root)

for (dirname, dirs, files) in allfiles:
    for file in files:
        if file.endswith(".py"):
            print_file(dirname + "\\" + file)
