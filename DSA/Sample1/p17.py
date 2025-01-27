#Python Program to Count the Number of Vowels in a String.
def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

string = input("Enter a string: ")
vowel_count = count_vowels(string)

print("The number of vowels in the string is: " + str(vowel_count))
