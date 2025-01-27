#Python Program to check whether a full pattern (not sub string) is present in the given sentence
def is_full_pattern_present(sentence, pattern):
    return sentence == pattern

sentence = input("Enter the sentence: ")
pattern = input("Enter the pattern: ")
result = is_full_pattern_present(sentence, pattern)

print("Is the full pattern present? " + str(result))
