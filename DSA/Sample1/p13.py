#Python Program to print the number of occurrence of a sub string in a given string
def count_substring_occurrences(string, substring):
    return string.count(substring)

string = input("Enter the main string: ")
substring = input("Enter the substring: ")
occurrences = count_substring_occurrences(string, substring)

print("The number of occurrences of the substring is: " + str(occurrences))