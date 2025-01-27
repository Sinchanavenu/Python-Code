#Python Program to Reverse a Given Number.
def reverse_number(n):
    return int(str(n)[::-1])

n = int(input("Enter an integer: "))
reversed_number = reverse_number(n)

print("The reversed number is: " + str(reversed_number))