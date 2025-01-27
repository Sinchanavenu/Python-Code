#Write a program sumfile.py that takes a filename as argument and prints sum of all numbers in that file. It is assumed that the file will only have one number in every line.
import sys
def sumfile(filename):
    try:
        with open(filename, 'r') as file:
            total_sum = sum(int(line.strip()) for line in file)
            print("Sum of all numbers: " + str(total_sum))
    except FileNotFoundError:
        print("File " + filename + " not found.")
    except ValueError:
        print("File contains non-numeric data.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sumfile.py <filename>")
    else:
        sumfile(sys.argv[1])

