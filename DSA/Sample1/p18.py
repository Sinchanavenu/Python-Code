#Python Program to Take in a String and Replace Every Blank Space with Hyphen.
def replace_spaces_with_hyphen(string):
    return string.replace(' ', '-')

string = input("Enter a string: ")
modified_string = replace_spaces_with_hyphen(string)

print("The modified string is: " + modified_string)
