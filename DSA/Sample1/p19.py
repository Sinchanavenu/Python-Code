#Python Program to find the length of string without using any built-in functions.
def manual_length(string):
    length = 0
    for char in string:
        length += 1
    return length

string = input("Enter a string: ")
length = manual_length(string)

print("The length of the string is: " + str(length))
