#Write a program find-matching-files.py to find files recursively in a directory tree matching given wildcard pattern. The program should accept the directory and the pattern as command-line argument
import sys
import os
import fnmatch

def find_matching_files(directory, pattern):
    matches = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if fnmatch.fnmatch(file, pattern):
                matches.append(os.path.join(root, file))
    return matches

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python find-matching-files.py <directory> <pattern>")
    else:
        directory = sys.argv[1]
        pattern = sys.argv[2]
        matches = find_matching_files(directory, pattern)
        for match in matches:
            print(match)
