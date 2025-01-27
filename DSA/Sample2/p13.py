#Python Program to Check if a Given Key Exists in a Dictionary or Not
def key_exists(dictionary, key):
    return key in dictionary

my_dict = eval(input("Enter a dictionary: "))
key = input("Enter the key to check: ")
result = key_exists(my_dict, key)
print("Does the key exist? " + str(result))