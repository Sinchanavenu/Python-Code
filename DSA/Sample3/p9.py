#Write a program most-recent-file.py to find the most recently modified file in the given directory. The program should accept the directory name as command-line argument and print path to the file (not just filename) that is most recently modified file
import sys
import os

def find_most_recent_file(directory):
    most_recent_file = None
    latest_time = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            mtime = os.path.getmtime(path)
            if mtime > latest_time:
                latest_time = mtime
                most_recent_file = path
    return most_recent_file

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python most-recent-file.py <directory>")
    else:
        directory = sys.argv[1]
        most_recent_file = find_most_recent_file(directory)
        print("Most recently modified file: " + str(most_recent_file))
