#Write an efficient code to remove duplicate elements from single linked list (you can make use of built in data structure "set")
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

    def remove_duplicates(self):
        if not self.head:
            return
        
        seen = set()
        current = self.head
        seen.add(current.data)
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next  # Remove the duplicate node
            else:
                seen.add(current.next.data)
                current = current.next

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

llist.remove_duplicates()

print("List after removing duplicates:")
llist.display()