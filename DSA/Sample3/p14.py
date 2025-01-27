#Write a function dups to find all duplicates in the list
def dups(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

elements = list(map(int, input("Enter elements separated by spaces: ").split()))
duplicates = dups(elements)
print("Duplicate elements: " + str(duplicates))
