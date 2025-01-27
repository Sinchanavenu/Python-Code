#Python Program to Remove the Duplicate Items from a List
def remove_duplicates(lst):
    return list(set(lst))

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_numbers = remove_duplicates(numbers)
print("List after removing duplicates: " + str(unique_numbers))