#Implement "FlexiQueue" with capacity to expand and shrunk based on elements to be added or deleted
class FlexiQueue:
    def __init__(self, initial_capacity=2):
        self.queue = []
        self.capacity = initial_capacity

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        if len(self.queue) >= self.capacity:
            self._expand_capacity()
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        
        item = self.queue.pop(0)
        if len(self.queue) <= self.capacity // 2 and self.capacity > 2:
            self._shrink_capacity()
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def _expand_capacity(self):
        self.capacity *= 2
        print("Queue capacity expanded to:", self.capacity)

    def _shrink_capacity(self):
        self.capacity //= 2
        print("Queue capacity shrunk to:", self.capacity)

    def __str__(self):
        return str(self.queue)

if __name__ == "__main__":
    q = FlexiQueue()
    print("Initial capacity:", q.capacity)
    q.enqueue(1)
    q.enqueue(2)
    print("Queue:", q)
    q.enqueue(3)
    print("Queue after expansion:", q)
    print("Dequeue:", q.dequeue())
    print("Queue:", q)
    q.dequeue()
    print("Queue after shrinking:", q)
    print("Queue size:", q.size())