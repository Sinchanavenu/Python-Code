#Python Program to Find the Second Largest Number in a List
def find_second_largest(lst):
    unique_numbers = list(set(lst)) 
    unique_numbers.sort(reverse=True)  
    return unique_numbers[1] if len(unique_numbers) > 1 else None

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
second_largest = find_second_largest(numbers)
print("The second largest number is: " + str(second_largest))