#Write a program copyfile.py to copy one file to another. It should accept two filenames as command-line arguments and copies the first one into the second
import sys
import shutil

def copyfile(source, destination):
    try:
        shutil.copy(source, destination)
        print("Copied " + source + " to " + destination)
    except FileNotFoundError:
        print("File " + source + " not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python copyfile.py <source> <destination>")
    else:
        copyfile(sys.argv[1], sys.argv[2])
