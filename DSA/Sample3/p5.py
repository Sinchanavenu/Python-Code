#Write a program grep.py that takes a pattern and a filename as command-line argument and prints all the lines in the file that contain given pattern.
import sys
def grep(pattern, filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if pattern in line:
                    print(line, end='')
    except FileNotFoundError:
        print("File " + filename + " not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <filename>")
    else:
        grep(sys.argv[1], sys.argv[2])
