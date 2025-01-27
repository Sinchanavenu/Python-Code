#Find the sum of last 'n' nodes in single linked list. Where 'n' will be given. Sum should be calculated with one iteration.
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

    def sum_of_last_n_nodes(self, n):
        main_ptr = self.head
        ref_ptr = self.head
        for _ in range(n):
            if ref_ptr is None:
                return 0
            ref_ptr = ref_ptr.next
        while ref_ptr:
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next
        total_sum = 0
        while main_ptr:
            total_sum += main_ptr.data
            main_ptr = main_ptr.next
        return total_sum

llist = LinkedList()
data_list = list(map(int, input("Enter the elements of the linked list: ").split()))
for data in data_list:
    llist.append(data)

n = int(input("Enter the value of n: "))
result = llist.sum_of_last_n_nodes(n)
print(f"Sum of last {n} nodes: {result}")
