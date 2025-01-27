#Python Program to Calculate the Average of Numbers in a Given List
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
average = calculate_average(numbers)

print("The average is: " + str(average))