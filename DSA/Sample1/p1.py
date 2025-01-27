#Program to exchange the values of two numbers without using a temporary variable
def swap(a,b):
    print("Before swapping: a=" ,a, "b=" ,b)
    a,b = b,a

    print("After swapping: a=", a, "b=" , b)
    return a,b

a= int(input())
b= int(input())

a,b=swap(a,b)