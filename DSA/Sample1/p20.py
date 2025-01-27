#Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions.
def larger_string(string1, string2):
    if len(string1) > len(string2):
        return string1
    else:
        return string2
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
larger = larger_string(string1, string2)

print("The larger string is: " + larger)
