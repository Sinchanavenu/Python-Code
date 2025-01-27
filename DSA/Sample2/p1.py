#Python Program to Find the Largest Number in a List
def find_largest(lst):
    return max(lst)
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
largest_number = find_largest(numbers)
print("The largest number is: " + str(largest_number))