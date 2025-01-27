#Python Program to Read a number n and Compute n+nn+nnn
def compute_nnn(n):
    return int(n) + int(n*2) + int(n*3)

n = input("Enter an integer: ")
result = compute_nnn(n)

print("The result of n + nn + nnn is: " + str(result))