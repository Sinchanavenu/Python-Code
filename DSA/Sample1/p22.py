#Python Program to Calculate the Number of Digits and Letters in a String.
def count_digits_and_letters(string):
    digit_count = sum(1 for char in string if char.isdigit())
    letter_count = sum(1 for char in string if char.isalpha())
    return digit_count, letter_count

string = input("Enter a string: ")
digit_count, letter_count = count_digits_and_letters(string)

print("Number of digits: " + str(digit_count))
print("Number of letters: " + str(letter_count))
