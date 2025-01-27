#Python Program to Find the Intersection of Lists
def intersection_of_lists(lst1, lst2):
    return list(set(lst1) & set(lst2))

list1 = list(map(int, input("Enter the first list of numbers separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list of numbers separated by spaces: "). split()))
intersection_result = intersection_of_lists(list1, list2)
print("Intersection of the lists: " + str(intersection_result))