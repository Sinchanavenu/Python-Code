#Write a Function is_empty(my_dict) that Takes a Dictionary my_dict and Returns True if my_dict is Empty and False Otherwise
def is_empty(my_dict):
    return not bool(my_dict)

my_dict = eval(input("Enter a dictionary: "))
result = is_empty(my_dict)
print("Is the dictionary empty? " + str(result))