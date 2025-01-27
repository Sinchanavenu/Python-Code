#Python Program to Put Even and Odd Elements in a List into Two Different Lists
def split_even_odd(lst):
    evens = [num for num in lst if num % 2 == 0]
    odds = [num for num in lst if num % 2 != 0]
    return evens, odds
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
evens, odds = split_even_odd(numbers)
print("Even numbers: " + str(evens))
print("Odd numbers: " + str(odds))