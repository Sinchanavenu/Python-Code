#Python program that reads two numbers from the user and prints their quotient and remainder
def cal_quo_remainder(a,b):
    quotient = a//b
    remainder = a%b
    return quotient, remainder
a= int(input())
b=int(input())
quotient, remainder = cal_quo_remainder(a,b)
print(quotient, remainder)