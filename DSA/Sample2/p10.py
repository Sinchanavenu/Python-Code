#Python Program to Read a List of Words and Return the Length of the Longest One
def length_of_longest_word(words):
    return max(len(word) for word in words)

words = input("Enter words separated by spaces: ").split()
longest_word_length = length_of_longest_word(words)
print("Length of the longest word: " + str(longest_word_length))