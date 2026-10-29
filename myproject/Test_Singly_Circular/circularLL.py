# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            # round and round because it called it's self. and make the round
            self.head = new_node
            new_node.next = self.head # cafusing line 50 -> 10
                                                    #temp  head
        else:
            temp = self.head

            while temp.next != self.head: # 
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

        print(data, "inserted at beginning.")

    # 2. Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
             # round and round because it called it's self. and make the round
            self.head = new_node
            new_node.next = self.head # cafusing line 50 -> 10
                                                    #temp  head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node # temp at last and insert into temp. 
            new_node.next = self.head # cafusing line 10 -> 50
                                                    #temp  head

        print(data, "inserted at end.")

    # 3. Insert at specific position
    def insert_position(self, data, position):
        if position < 1:
            print("Invalid position.")
            return

        if position == 1:
            self.insert_beginning(data)
            return

        if self.head is None:
            print("Invalid position.")
            return

        temp = self.head # connect to start piont of node ex:- 60 -> 10
        current_position = 1 # user input 

        while current_position < position - 1: # 1 less than (2)-1
                                               # 1 = 1
            temp = temp.next
            current_position += 1 # increment on cuurent position

            if temp == self.head:
                print("Invalid position.")
                return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

        print(data, "inserted at position", position)

    # 4. Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("Circular linked list is empty.")
            return

        deleted_data = self.head.data

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            self.head = self.head.next
            temp.next = self.head

        print(deleted_data, "deleted from beginning.")

    # 5. Delete from end
    def delete_end(self):
        if self.head is None:
            print("Circular linked list is empty.")
            return

        if self.head.next == self.head:
            deleted_data = self.head.data
            self.head = None
            print(deleted_data, "deleted from end.")
            return

        temp = self.head

        while temp.next.next != self.head:
            temp = temp.next

        deleted_data = temp.next.data
        temp.next = self.head

        print(deleted_data, "deleted from end.")

    # 6. Delete a node by value
    def delete_value(self, value):
        if self.head is None:
            print("Circular linked list is empty.")
            return

        current = self.head
        previous = None

        while True:
            if current.data == value:

                # Only one node
                if current.next == self.head and current == self.head:
                    self.head = None

                # Delete the first node
                elif current == self.head:
                    last = self.head

                    while last.next != self.head:
                        last = last.next

                    self.head = self.head.next
                    last.next = self.head

                # Delete any other node
                else:
                    previous.next = current.next

                print(value, "deleted from circular linked list.")
                return

            previous = current
            current = current.next

            if current == self.head:
                break

        print(value, "not found in circular linked list.")

    # 7. Search for an element
    def search(self, value):
        if self.head is None:
            print("Circular linked list is empty.")
            return

        temp = self.head
        position = 1

        while True:
            if temp.data == value:
                print(value, "found at position", position)
                return

            temp = temp.next
            position += 1

            if temp == self.head:
                break

        print(value, "not found in circular linked list.")

    # 8. Count the number of nodes
    def count_nodes(self):
        if self.head is None:
            print("Total number of nodes: 0")
            return

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Total number of nodes:", count)

    # 9. Reverse the circular linked list
    def reverse(self):
        if self.head is None:
            print("Circular linked list is empty.")
            return

        if self.head.next == self.head:
            print("Circular linked list reversed.")
            return

        previous = None
        current = self.head
        old_head = self.head

        while True:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

            if current == old_head:
                break

        old_head.next = previous
        self.head = previous

        print("Circular linked list reversed.")

    # 10. Display the circular linked list
    def display(self):
        if self.head is None:
            print("Circular linked list is empty.")
            return

        temp = self.head

        print("Circular Linked List:", end=" ")

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")

    # 11. Display in reverse order without modifying the list
    def display_reverse(self):
        if self.head is None:
            print("Circular linked list is empty.")
            return

        values = []
        temp = self.head

        while True:
            values.append(temp.data)
            temp = temp.next

            if temp == self.head:
                break

        print("Reverse Order:", end=" ")

        for value in reversed(values):
            print(value, end=" -> ")

        print("(back to tail)")


# Main Program
linked_list = CircularLinkedList()

while True:
    print("\n======= CIRCULAR LINKED LIST =======")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Specific Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete by Value")
    print("7. Search an Element")
    print("8. Count Nodes")
    print("9. Reverse Circular Linked List")
    print("10. Display Circular Linked List")
    print("11. Display in Reverse Order")
    print("12. Exit")
    print("====================================")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        data = int(input("Enter data: "))
        linked_list.insert_beginning(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        linked_list.insert_end(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        position = int(input("Enter position: "))
        linked_list.insert_position(data, position)

    elif choice == 4:
        linked_list.delete_beginning()

    elif choice == 5:
        linked_list.delete_end()

    elif choice == 6:
        value = int(input("Enter value to delete: "))
        linked_list.delete_value(value)

    elif choice == 7:
        value = int(input("Enter value to search: "))
        linked_list.search(value)

    elif choice == 8:
        linked_list.count_nodes()

    elif choice == 9:
        linked_list.reverse()

    elif choice == 10:
        linked_list.display()

    elif choice == 11:
        linked_list.display_reverse()

    elif choice == 12:
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")
