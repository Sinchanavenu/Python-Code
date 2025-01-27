# Write a program to generate 10 random integers
import random

def generate_random_integers(count):
    return [random.randint(0, 100) for _ in range(count)]

random_numbers = generate_random_integers(10)
print("10 random integers: " + str(random_numbers))
