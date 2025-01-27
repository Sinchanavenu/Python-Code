#Python Program to Add a Key-Value Pair to the Dictionary
def add_key_value(dictionary, key, value):
    dictionary[key] = value
    return dictionary

my_dict = {}
key = input("Enter the key: ")
value = input("Enter the value: ")
updated_dict = add_key_value(my_dict, key, value)
print("Updated dictionary: " + str(updated_dict))