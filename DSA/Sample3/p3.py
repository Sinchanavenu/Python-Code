#Write a program head.py that takes a filename as command-line argument and prints the first 5 lines of it
import sys

def head(filename):
    try:
        with open(filename, 'r') as file:
            for i in range(5):
                line = file.readline()
                if not line:
                    break
                print(line, end='')
    except FileNotFoundError:
        print("File " + filename + " not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python head.py <filename>")
    else:
        head(sys.argv[1])
