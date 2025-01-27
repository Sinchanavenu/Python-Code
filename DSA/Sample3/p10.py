#Write a program files-only.py to find only file and not sub directories. Pass directory name as command line argument
import sys
import os

def files_only(directory):
    try:
        for item in os.listdir(directory):
            path = os.path.join(directory, item)
            if os.path.isfile(path):
                print(item)
    except FileNotFoundError:
        print("Directory " + directory + " not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python files-only.py <directory>")
    else:
        files_only(sys.argv[1])
