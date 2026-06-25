# Creating a Single Linked List
# Create Nodes
# Append Nodes
# Prepend Nodes
# Print the elements in a single linked list
 
# creating a Node
class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

# a = Node(1) # node a
# b = Node(2) # node b
# a.next = b # linking node b to a
# print(a.next.value)

class LinkedList:
    def __init__ (self):
        self.head = None # initializing head to None
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def print_list(self):
        if self.head is None:
            print("Empty List")
            return
        current = self.head
        while current is not None:
            print(current.value, end="->")
            current = current.next
        print("None")

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.prepend(0)
l1.print_list()

