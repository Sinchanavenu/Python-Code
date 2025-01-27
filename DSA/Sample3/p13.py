#Write a function unique to find all the unique elements of a list
def unique(lst):
    return list(set(lst))

elements = list(map(int, input("Enter elements separated by spaces: ").split()))
unique_elements = unique(elements)
print("Unique elements: " + str(unique_elements))
