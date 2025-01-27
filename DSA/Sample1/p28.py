#Write a program to generate 10 random numbers between 1 to 100 such that there should one number between 1 to 10 one number between 11 to 20 etc
import random

def generate_random_numbers_distributed():
    return [random.randint(i, i+9) for i in range(1, 101, 10)]

random_numbers = generate_random_numbers_distributed()
print("10 random numbers with specific distribution: " + str(random_numbers))
