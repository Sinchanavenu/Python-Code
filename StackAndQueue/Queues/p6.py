#Assume that we have Queue with some elements. Write menthod rotate() which added the existing elements in the reverse order
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def rotate(self):
        temp = self.queue[::-1]
        self.queue = []
        for item in temp:
            self.enqueue(item)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print("Before Rotation:",q.queue)
q.rotate()
print("After Rotation:",q.queue)