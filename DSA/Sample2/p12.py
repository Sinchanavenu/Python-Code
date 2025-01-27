#Python Program to Concatenate Two Dictionaries Into One
def concatenate_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

dict1 = eval(input("Enter the first dictionary: "))
dict2 = eval(input("Enter the second dictionary: "))
concatenated_dict = concatenate_dictionaries(dict1, dict2)
print("Concatenated dictionary: " + str(concatenated_dict))