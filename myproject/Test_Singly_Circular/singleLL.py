class Node:
    def __init__(self, data):
        self.data = data      # value stored in the node
        self.next = None      # address of the next node (None = end of list)


class SinglyLinkedList:
    def __init__(self):
        self.head = None      # empty list -> head points to nothing

    # 1. Insert at the end
    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            
        else:
            temp = self.head
            while temp.next is not None:   # walk to the last node
                temp = temp.next
            temp.next = new_node
        print(data, "inserted at the last.")

    # 2. Insert at the beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head          # new node points to the old first node
        self.head = new_node               # head now points to the new node
        print(data, "inserted at the beginning.")

    # 3. Insert at a position (position starts from 1)
    def insert_position(self, data, position):
        if position < 1:
            print("Position must be 1 or more.")
        elif position == 1:
            self.insert_begin(data)
        else:
            temp = self.head
            count = 1
            while temp is not None and count < position - 1:
                temp = temp.next           # stop at the node BEFORE the position
                count += 1
            if temp is None:
                print("Position is out of range.")
            else:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                print(data, "inserted at position", position)

    # 4. Display the list
    def display(self):
        if self.head is None:
            print("List is empty.")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

    # 5. Search a value
    def search_value(self, value):
        temp = self.head
        position = 1
        while temp is not None:
            if temp.data == value:
                print(value, "found at position", position)
                return
            temp = temp.next
            position += 1
        print(value, "not found in the list.")

    # 6. Count the nodes
    def count_value(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        print("Total nodes:", count)

    # 7. Delete the first node having this value
    def delete_value(self, value):
        if self.head is None:
            print("List is empty.")
        elif self.head.data == value:
            self.head = self.head.next     # first node is removed
            print(value, "deleted.")
        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.data == value:
                    temp.next = temp.next.next   # skip the node to delete
                    print(value, "deleted.")
                    return
                temp = temp.next
            print(value, "not found in the list.")

    # 8. Delete the first node
    def delete_begin(self):
        if self.head is None:
            print("List is empty.")
        else:
            print(self.head.data, "deleted from the beginning.")
            self.head = self.head.next

    # 9. Reverse the list
    def reverse_operation(self):
        if self.head is None:
            print("List is empty.")
        else:
            previous = None
            current = self.head
            while current is not None:
                next_node = current.next   # save the next node
                current.next = previous    # reverse the link
                previous = current         # move previous forward
                current = next_node        # move current forward
            self.head = previous
            print("List reversed.")


ll = SinglyLinkedList()

while True:
    print("\n----- Singly Linked List Menu -----")
    print("1. Insert at last")
    print("2. Insert at beginning")
    print("3. Insert at position")
    print("4. Display")
    print("5. Search value")
    print("6. Count nodes")
    print("7. Delete value")
    print("8. Delete from beginning")
    print("9. Reverse list")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = int(input("Enter value: "))
        ll.insert_last(data)
    elif choice == "2":
        data = int(input("Enter value: "))
        ll.insert_begin(data)
    elif choice == "3":
        data = int(input("Enter value: "))
        position = int(input("Enter position: "))
        ll.insert_position(data, position)
    elif choice == "4":
        ll.display()
    elif choice == "5":
        value = int(input("Enter value to search: "))
        ll.search_value(value)
    elif choice == "6":
        ll.count_value()
    elif choice == "7":
        value = int(input("Enter value to delete: "))
        ll.delete_value(value)
    elif choice == "8":
        ll.delete_begin()
    elif choice == "9":
        ll.reverse_operation()
    elif choice == "10":
        print("Program ended.")
        break
    else:
        print("Invalid choice, please enter 1 to 10.")