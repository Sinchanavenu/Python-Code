#Implement Queue using two stacks
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = [] 
        self.stack2 = []  

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2[-1]

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def __str__(self):
        if self.stack2:
            return str(self.stack2[::-1] + self.stack1)
        return str(self.stack1)

if __name__ == "__main__":
    queue = QueueUsingStacks()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Queue:", queue)

    print("Dequeued element:", queue.dequeue())
    print("Queue after dequeue:", queue)

    queue.enqueue(40)
    print("Queue after enqueue:", queue)

    print("Front element:", queue.peek())
    print("Queue size:", queue.size())