#Implement a function with signature transfer(S,T).This function transfers all elemnts from Stack S to Stack T. The sequence of elements in T should be same as that of S.
def transfer(S, T):
    temp_stack = []
    
    while S:
        temp_stack.append(S.pop())
    
    while temp_stack:
        T.append(temp_stack.pop())

def get_stack_input(stack_name):
    n = int(input("Enter the number of elements in stack " + stack_name + ": "))
    stack = []
    print("Enter the elements for stack " + stack_name + ":")
    for _ in range(n):
        element = input()
        stack.append(element)
    return stack


S = get_stack_input("S")


T = get_stack_input("T")

print("\nS before transfer: " + str(S))
print("T before transfer: " + str(T))

transfer(S, T)

print("\nS after transfer: " + str(S))
print("T after transfer: " + str(T))
