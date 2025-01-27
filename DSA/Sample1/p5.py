#Program to print all odd numbers in a given range
def print_odd_num(start ,end):
    for num in range( start, end+1):
        if num%2!=0:
            print(num, end=" ")

start=int(input())
end=int(input())
print_odd_num(start, end)