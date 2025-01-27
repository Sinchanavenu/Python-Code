#Write a Function make_dict(key_value_list) that Takes a List of Tuples key_value_list Where Each Tuple is of the Form (key, value) and Returns a Dictionary with These Keys and Corresponding Values
def make_dict(key_value_list):
    return dict(key_value_list)

key_value_list = eval(input("Enter a list of tuples (e.g., [('a', 1), ('b', 2)]): "))
result_dict = make_dict(key_value_list)
print("Resulting dictionary: " + str(result_dict))