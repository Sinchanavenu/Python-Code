#Write a program cat.py that takes a filename as command-line argument and prints all the contents of that file
import sys
def cat(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("File " + filename + " not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cat.py <filename>")
    else:
        cat(sys.argv[1])
