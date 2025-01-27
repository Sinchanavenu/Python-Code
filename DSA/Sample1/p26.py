#Write a program to generate 10 random integers between 1 to 20 (both inclusive)
import random

def generate_random_integers_range(count, start, end):
    return [random.randint(start, end) for _ in range(count)]

random_numbers = generate_random_integers_range(10, 1, 20)
print("10 random integers between 1 and 20: " + str(random_numbers))
