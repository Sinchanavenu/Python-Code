#Write a Function make_cipher_dict(alphabet) that Takes a String of Unique Characters and Returns a Randomly-Generated Cipher Dictionary for the Characters in alphabet
import random

def make_cipher_dict(alphabet):
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    return dict(zip(alphabet, shuffled_alphabet))

alphabet = input("Enter a string of unique characters: ")
cipher_dict = make_cipher_dict(alphabet)
print("Generated cipher dictionary: " + str(cipher_dict))