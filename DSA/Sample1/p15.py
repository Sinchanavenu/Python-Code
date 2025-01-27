#Python Program to return true if all characters in the string are alphabetic and there is at least one other character, False.
def is_alpha_and_non_empty(string):
    return string.isalpha() and len(string) > 0

string = input("Enter a string: ")
result = is_alpha_and_non_empty(string)

print("All characters are alphabetic and there's at least one character: " + str(result))
