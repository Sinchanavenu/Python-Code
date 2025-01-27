#Implement limited size stack
class LimitedSizeStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def stackCount(self):
        return self.count

    def stackPush(self, ele):
        if self.count < self.capacity:
            self.data.append(ele)
            self.count += 1
        else:
            raise OverflowError("Push attempted on a full stack.")

    def stackPop(self):
        if not self.isEmpty():
            self.count -= 1
            return self.data.pop()
        else:
            return None

    def stackPeek(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            return None

    def __str__(self):
        return str(self.data)


stack = LimitedSizeStack(3)  
stack.stackPush(1)
stack.stackPush(2)
stack.stackPush(3)

print(stack)               
print(stack.stackPeek())  

try:
    stack.stackPush(4)   
except OverflowError as e:
    print(e)

print(stack.stackPop())  
print(stack)             

print(stack.isEmpty()) 