#Python Program to Sum All the Items in a Dictionary
def sum_dictionary_items(dictionary):
    return sum(dictionary.values())

my_dict = eval(input("Enter a dictionary: "))
total_sum = sum_dictionary_items(my_dict)
print("Sum of all items: " + str(total_sum))