#Assume that we have two linked lists. Elements in individual list are unique. There maybe identical elements across linked lists. Create a third list which contains only common elements across the first two lists.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)) if elements else "List is empty")

    def to_set(self):
        result_set = set()
        current = self.head
        while current:
            result_set.add(current.data)
            current = current.next
        return result_set

def create_common_list(list1, list2):
    set1 = list1.to_set()
    set2 = list2.to_set()
    
    common_elements = set1.intersection(set2)
    
    common_list = LinkedList()
    for element in common_elements:
        common_list.add_tail(element)
    
    return common_list

list1 = LinkedList()
list1.add_tail(1)
list1.add_tail(2)
list1.add_tail(3)
list1.add_tail(4)

list2 = LinkedList()
list2.add_tail(3)
list2.add_tail(4)
list2.add_tail(5)
list2.add_tail(6)

common_list = create_common_list(list1, list2)
print("Common elements in the third list:")
common_list.display()
