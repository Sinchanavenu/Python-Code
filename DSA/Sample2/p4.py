#Python Program to Check Whether Two Lists are the Same
def are_lists_same(lst1, lst2):
    return lst1 == lst2

list1 = list(map(int, input("Enter the first list of numbers separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list of numbers separated by spaces: ").split()))
result = are_lists_same(list1, list2)
print("Are the two lists the same? " + str(result))