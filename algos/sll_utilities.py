# SLL Utilities

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_front(self, data):
        new_node = SLNode(data)
        # Save the current head in a variable
        current_head = self.head

        # Set the new node's next to the list current head
        new_node.next = current_head

        # Set the list's head to the node we created in the las step
        self.head = new_node
        return self

# Add a method contains(value) to your SLL class, which is given a value as a parameter.  Return a boolean (true/false); true, if the list possesses a node that contains the provided value.

    def contains(self, val):
        if self.head != None:
            current_node = self.head
            while current_node.value != val  :
