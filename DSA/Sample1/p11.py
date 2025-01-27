#Python Program to Count the Number of Digits in a Number.
def count_digits(n):
    return len(str(n))

n = int(input("Enter an integer: "))
digit_count = count_digits(n)

print("The number of digits in the number is: " + str(digit_count))