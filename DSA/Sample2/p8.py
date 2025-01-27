#Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number
def create_tuples(lst):
    return [(num, num**2) for num in lst]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
tuple_list = create_tuples(numbers)
print("List of tuples: " + str(tuple_list))