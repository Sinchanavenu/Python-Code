#Cumulative sum of a list [1, 2, 4, …] is defined as [1, 3, 7, . . .] Write a function cumulative_sum() to compute cumulative sum of a list
def cumulative_sum(lst):
    cumsum = []
    total = 0
    for num in lst:
        total += num
        cumsum.append(total)
    return cumsum

numbers = input()
cumulative_result = cumulative_sum(numbers)
print("Cumulative sum: " + str(cumulative_result))
