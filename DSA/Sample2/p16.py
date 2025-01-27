#Python Program to Multiply All the Items in a Dictionary
def multiply_dictionary_items(dictionary):
    result = 1
    for value in dictionary.values():
        result *= value
    return result

my_dict = eval(input("Enter a dictionary: "))
total_product = multiply_dictionary_items(my_dict)
print("Product of all items: " + str(total_product))