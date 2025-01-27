#Python Program to Check if a Number is a Palindrome.
def is_palindrome(n):
    return n == n[::-1]

n = input("Enter an integer: ")
palindrome_check = is_palindrome(n)

print("Is the number a palindrome? " + str(palindrome_check))
