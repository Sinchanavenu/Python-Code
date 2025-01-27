#Implement "Simple Queue" using list data structure
class SimpleQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

if __name__ == "__main__":
    q = SimpleQueue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Queue:", q) 

    print("Dequeue:", q.dequeue())  
    print("Peek:", q.peek())        

    print("Queue:", q)  

    print("Size of queue:", q.size())  

    q.dequeue()
    q.dequeue()