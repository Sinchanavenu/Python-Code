#Write a program ls.py that takes path to a directory as command-line argument and prints all the files in that directory. When no argument is specified, it should list the files in the current directory
import sys
import os

def ls(directory='.'):
    try:
        files = os.listdir(directory)
        for file in files:
            print(file)
    except FileNotFoundError:
        print("Directory " + directory + " not found.")

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    ls(directory)
