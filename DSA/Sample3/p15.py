#Write a function group(list, size) that take a list and splits into smaller lists of given size
def group(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

elements = list(map(int, input("Enter elements separated by spaces: ").split()))
size = int(input("Enter group size: "))
grouped = group(elements, size)
print("Grouped elements: " + str(grouped))
