#Write a program find-large-files.py to find files recursively in a directory tree that are larger than given size. The program should accept the directory and the size as command-line argument. The size can be also be specified with K, M and G suffix for KB, MB and GB respectively
import sys
import os

def convert_size(size_str):
    size_str = size_str.upper()
    if size_str.endswith('K'):
        return int(size_str[:-1]) * 1024
    elif size_str.endswith('M'):
        return int(size_str[:-1]) * 1024 * 1024
    elif size_str.endswith('G'):
        return int(size_str[:-1]) * 1024 * 1024 * 1024
    else:
        return int(size_str)

def find_large_files(directory, size):
    min_size = convert_size(size)
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            if os.path.getsize(path) > min_size:
                print(path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python find-large-files.py <directory> <size>")
    else:
        directory = sys.argv[1]
        size = sys.argv[2]
        find_large_files(directory, size)
