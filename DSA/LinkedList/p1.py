#Create a single linked list class withe the following functionalities: 
#Add a head
#Add a tail
#Delete at head
#Delete at tail
#Add afer given data
#Delete after given data
#Search an element
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def add_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def delete_head(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next
    
    def delete_tail(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
    
    def add_after(self, target_data, new_data):
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node with data {target_data} not found")
    
    def delete_after(self, target_data):
        current = self.head
        while current and current.next:
            if current.data == target_data:
                current.next = current.next.next
                return
            current = current.next
        print(f"Node with data {target_data} not found or no node after it")
    
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)) if elements else "List is empty")

ll = LinkedList()
ll.add_head(10)
ll.add_tail(20)
ll.add_tail(30)
ll.display()
ll.add_after(20, 25)
ll.delete_head()
ll.delete_tail()
ll.delete_after(20)
print("Search 25:", ll.search(25))
print("Search 20:", ll.search(20))
ll.display()
