#Python Program to Generate a Dictionary that Contains Numbers (Between 1 and n) in the Form (x, x*x)
def generate_square_dict(n):
    return {x: x*x for x in range(1, n+1)}

n = int(input("Enter the value of n: "))
square_dict = generate_square_dict(n)
print("Dictionary of squares: " + str(square_dict))