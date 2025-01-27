#Find whether linked list contains cycle
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True  # Cycle detected
        
        return False  # No cycle detected

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

llist = LinkedList()
data_list = list(map(int, input("Enter the elements of the linked list: ").split()))
for data in data_list:
    llist.append(data)

if llist.detect_cycle():
    print("The linked list contains a cycle.")
else:
    print("The linked list does not contain a cycle.")
