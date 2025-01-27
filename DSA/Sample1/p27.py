#   Write a program to generate 5 random integers between 1 to 20 such that numbers should be unique
import random

def generate_unique_random_integers(count, start, end):
    return random.sample(range(start, end + 1), count)

random_numbers = generate_unique_random_integers(5, 1, 20)
print("5 unique random integers between 1 and 20: " + str(random_numbers))
