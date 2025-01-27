#Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String.
def count_upper_and_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

string = input("Enter a string: ")
upper_count, lower_count = count_upper_and_lower(string)

print("Number of upper case letters: " + str(upper_count))
print("Number of lower case letters: " + str(lower_count))
