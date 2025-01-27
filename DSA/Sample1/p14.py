#Python program to print the lowest index in the string where substring sub is found within the string.
def find_lowest_index(string, substring):
    return string.find(substring)

string = input("Enter the main string: ")
substring = input("Enter the substring: ")
index = find_lowest_index(string, substring)

print("The lowest index where the substring is found is: " + str(index))
