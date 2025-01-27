#Python Program to Remove the Given Key from a Dictionary
def remove_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary

my_dict = eval(input("Enter a dictionary: "))
key = input("Enter the key to remove: ")
updated_dict = remove_key(my_dict, key)
print("Dictionary after removing key: " + str(updated_dict))