#Find middle element of linked list without iterating all elements
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

    def find_middle(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if slow:
            return slow.data
        return None

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

print("Original list:")
llist.display()

middle_element = llist.find_middle()
print(f"Middle element: {middle_element}")
