# Singly Linked Lists

# ---- Fronts ---- #

from unittest import runner


class SLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SList:
    def __init__(self, head):
        self.head = head

# Add Front
# Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node.

    def add_front(self, data):
        new_node = SLNode(data)
        # Save the current head in a variable
        current_head = self.head

        # Set the new node's next to the list current head
        new_node.next = current_head

        # Set the list's head to the node we created in the las step
        self.head = new_node
        return self

# Front
# Write a method to return the value (not the node) at the head of the list. If the list is empty, return null.

    def print_values(self):
        # A pointer to the list's first head
        runner = self.head

        # iterating while runner is a node and not None
        while(runner != None):
            # print the current node's value
            print(runner.data)
            # Set the runner to it's neighbor
            runner = runner.next
        return self

# Remove Front
# Write a method to remove the head node and return the new list head node. If the list is empty, return null.

    def remove_front(self):
        if self.head != None:
            self.head = self.head.next
        return self



# ----SLL Utilities---- #

# Add a method contains(value) to your SLL class, which is given a value as a parameter.  Return a boolean (true/false); true, if the list possesses a node that contains the provided value.

    def contains_value(self, data):
        if self.head != None:
            current_node = self.head
            while current_node.data != data :
                current_node = current_node.next
                if current_node.next == None:
                    print(data)
                    return False
            print(data), "in list"

# Display
# Create display() that returns a string containing all list values. Build what you wish console.log(myList) did!

    def display(self):
        runner = self.head
        node = 1
        while runner:
            print(f"This is node- {node} , Its value is - {runner.data}")
            node = node + 1
            runner = runner.next
            print(f' They are {node} total of nodes in the list')
        return self

# Length
# Create a new SLL method length() that returns number of nodes in that list.

    def length(self):
        length = 0
        runner = self.head
        while(runner != None):
            length+= 1
            runner = runner.next
        return length

# SList: Move Max to Back
# Create a standalone function that locates the maximum value in a linked list, and moves that node to the back of the list. Return the new list, with all nodes still present, and all in their original order except for the node you moved to the end of the singly linked list.

    def move_max(self):
        max_value = 0
        runner = self.head
        while runner:
            if runner.data > max_value:
                max_value = runner.data
            else:
                runner = runner.next
            print(f'The max value is-{max_value}')
        return max_value


# SList: Move Min to Front
# Create a standalone function that locates the minimum value in a linked list, and moves that node to the front of the list. Return the new list, with all nodes still present, and all (except for the new head node) in their original order.

    def min_front(self):
        min_value = self.head.data
        runner = self.head
        while runner:
            if runner.data < min_value:
                min_value = runner.data
            else:
                runner = runner.next
            print(f'The min value is- {min_value}')
        return min_value


#  Testing our classes
list = SList(SLNode(10))
list.add_front(1).add_front(25).add_front(10).add_front(89).remove_front().print_values().display().min_front()