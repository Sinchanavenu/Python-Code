#Implement findMax() method, which return the maximum value of element present in the queue. After finding maximum element, queue contet should be same as original.
class SimpleQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def findMax(self):
        if self.is_empty():
            raise ValueError("The queue is empty")

        max_value = self.queue[0] 

        for item in self.queue:
            if item > max_value:
                max_value = item

        return max_value

    def __str__(self):
        return str(self.queue)

if __name__ == "__main__":
    q = SimpleQueue()

    q.enqueue(1)
    q.enqueue(5)
    q.enqueue(3)
    q.enqueue(7)
    q.enqueue(2)

    print("Original Queue:", q)

    max_value = q.findMax()

    print("Maximum value in the queue:", max_value)
    print("Queue after findMax:", q)