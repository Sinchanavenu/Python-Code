#check whether given linked list is palindrome or not
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

    def is_palindrome(self):
        slow = self.head
        fast = self.head
        prev_slow = None
        stack = []

        while fast and fast.next:
            stack.append(slow.data)
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        if fast: 
            slow = slow.next

        while slow:
            top = stack.pop()
            if slow.data != top:
                return False
            slow = slow.next
        
        return True

llist = LinkedList()
data_list = list(map(int, input("Enter the elements of the linked list: ").split()))
for data in data_list:
    llist.append(data)

if llist.is_palindrome():
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")