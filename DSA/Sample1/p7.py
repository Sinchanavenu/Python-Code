#Program to find the smallest divisor of a given integer
def smallest_divisor(n):
    if n <= 1:
        return n
    for i in range(2, n+1):
        if n % i == 0:
            return i

number = int(input("Enter an integer: "))
divisor = smallest_divisor(number)

print("The smallest divisor of " + str(number) + " is " + str(divisor) + ".")