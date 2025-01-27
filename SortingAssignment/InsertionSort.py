#Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

input_str = input("Enter numbers separated by spaces: ")
arr = list(map(int, input_str.split()))
insertion_sort(arr)
print("Insertion Sort:", arr)