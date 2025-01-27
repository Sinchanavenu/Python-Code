#Implement Stack using two queues
from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        self.queue1.append(x)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        popped_item = self.queue1.popleft()

        self.queue1, self.queue2 = self.queue2, self.queue1

        return popped_item

    def top(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        top_item = self.queue1.popleft()
        self.queue2.append(top_item)

        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_item

    def is_empty(self):
        return len(self.queue1) == 0

    def size(self):
        return len(self.queue1) + len(self.queue2)

    def __str__(self):
        return str(list(self.queue1) + list(self.queue2))


if __name__ == "__main__":
    stack = StackUsingQueues()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack:", stack)

    print("Top element:", stack.top())
    print("Popped element:", stack.pop())
    print("Stack after pop:", stack)

    print("Top element:", stack.top())
    print("Popped element:", stack.pop())
    print("Stack after pop:", stack)