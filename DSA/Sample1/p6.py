#Program to find sum of digits of a number
def sum_of_digits(num):
    total=0
    while num>0:
        digit=num%10
        total+=digit
        num=num//10
    return total
num=int(input())
result=sum_of_digits(num)
print(result)