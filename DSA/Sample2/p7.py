#Python Program to Find Union and Intersection of Lists Without Repetition
def union_and_intersection(lst1, lst2):
    union_result = list(set(lst1) | set(lst2))
    intersection_result = list(set(lst1) & set(lst2))
    return union_result, intersection_result

list1 = list(map(int, input("Enter the first list of numbers separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list of numbers separated by spaces: ").split()))
union_result, intersection_result = union_and_intersection(list1, list2)
print("Union without repetition: " + str(union_result))
print("Intersection without repetition: " + str(intersection_result))