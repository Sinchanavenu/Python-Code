#Selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

input_str = input("Enter numbers separated by spaces: ")
arr = list(map(int, input_str.split()))
selection_sort(arr)
print("Selection Sort:", arr)