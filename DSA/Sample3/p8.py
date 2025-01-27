#Write a program largest-file.py to find the largest file in the given directory. The program should accept the directory name as command-line argument and print path to the file (not just filename)
import sys
import os

def find_largest_file(directory):
    largest_file = None
    max_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            if size > max_size:
                max_size = size
                largest_file = path
    return largest_file

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python largest-file.py <directory>")
    else:
        directory = sys.argv[1]
        largest_file = find_largest_file(directory)
        print("Largest file: " + str(largest_file))
