#Modify Q1 such that Simple Queue can contain limited amount of elements
class SimpleQueue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Enqueue to a full queue")
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
    q = SimpleQueue(capacity=3)

    print("Enqueue 1")
    q.enqueue(1)
    print("Queue:", q)

    print("Enqueue 2")
    q.enqueue(2)
    print("Queue:", q)

    print("Enqueue 3")
    q.enqueue(3)
    print("Queue:", q)

    print("Dequeue:", q.dequeue())
    print("Queue:", q)

    print("Enqueue 4")
    q.enqueue(4)
    print("Queue:", q)
    # q.enqueue(5)   This will give overflow error since capacity is 3
    # print("Queue:",q)

    print("Size of queue:", q.size())