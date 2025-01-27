#Program to check whether a number is positive or negative

def check_number(num):
    if num> 0:
        return "The number is positive"
    elif num <0:
        return "The number is negative"
    else:
        return "The number is zero"
num=float(input())
result=check_number(num)
print(result)