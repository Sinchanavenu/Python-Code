#Implement the split() function that splits given linked list into two two separate linked lists containing alternate elements from the original list
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

    def split(self):
        list1 = LinkedList()
        list2 = LinkedList()
        current = self.head
        alternate = True
        
        while current:
            if alternate:
                list1.append(current.data)
            else:
                list2.append(current.data)
            alternate = not alternate
            current = current.next
        
        return list1, list2

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

list1, list2 = llist.split()

print("First list (alternate elements):")
list1.display()

print("Second list (remaining alternate elements):")
list2.display()
