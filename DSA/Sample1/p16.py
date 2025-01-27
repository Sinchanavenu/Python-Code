#Python Program to Replace all Occurrences of ‘a’ with $ in a String.
def replace_a_with_dollar(string):
    return string.replace('a', '$')

string = input("Enter a string: ")
modified_string = replace_a_with_dollar(string)

print("The modified string is: " + modified_string)
