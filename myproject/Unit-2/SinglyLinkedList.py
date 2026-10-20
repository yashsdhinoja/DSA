class Node:
    def __init__(self, data):
        self.data = data      # Stores the actual value (e.g., 10, 20)
        self.next = None      # Stores the memory address of the next node (initially None)

class SLL:
    def __init__(self):
        self.head = None      # Points to the very first node of the list (initially empty)

# 1. Create an empty Linked List manager
my_list = SLL()
# 2. Create a node manually with data 10
first_node = Node(10)
# 3. Connect the list's head to this first node
my_list.head = first_node

print("Head data : ", my_list.head.data)
print("next pionter :", my_list.head.next)