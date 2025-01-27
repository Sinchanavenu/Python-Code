#Write a program wc.py that takes filename as argument and counts number of lines, words and chars in file.
import sys

def wc(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)
            print("Lines: " + str(num_lines))
            print("Words: " + str(num_words))
            print("Chars: " + str(num_chars))
    except FileNotFoundError:
        print("File " + filename + " not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wc.py <filename>")
    else:
        wc(sys.argv[1])
