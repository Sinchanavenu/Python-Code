#Write a Function encrypt(phrase, cipher_dict) that Takes a String phrase and a Dictionary cipher_dict and Returns the Result of Replacing Each Character in phrase by its Corresponding Value in cipher_dict
def encrypt(phrase, cipher_dict):
    return ''.join(cipher_dict.get(char, char) for char in phrase)

phrase = input("Enter the phrase to encrypt: ")
cipher_dict = eval(input("Enter the cipher dictionary: "))
encrypted_phrase = encrypt(phrase, cipher_dict)
print("Encrypted phrase: " + encrypted_phrase)