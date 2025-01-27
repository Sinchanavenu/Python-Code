#Implement unlimited size stack
class SimpleStack:
    def __init__(self):
        self.data=[]
        self.count=0
    def isEmpty(self):
        return self.count==0
    def stackCount(self):
        return self.count
    def stackPush(self, ele):
        self.data.append(ele)
        self.count+=1
    def stackPop(self):
        if not self.isEmpty():
            self.count-=1
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

stack = SimpleStack()
stack.stackPush(1)
stack.stackPush(2)
stack.stackPush(3)

print(stack)               
print(stack.stackPeek()) 
print(stack.stackPop())   
print(stack)               
print(stack.isEmpty()) 