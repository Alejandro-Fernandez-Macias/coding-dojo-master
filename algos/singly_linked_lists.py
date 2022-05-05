class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):	# added this line, takes a value
        new_node = SLNode(val)
        current_head = self.head    # save the current head in a variable
        new_node.next = current_head   # Set the new node's next to the list's current head
        self.head = new_node   # Set the list's head to the node we created in the last step
        return self  # return self to allow for chaining

    def print_values(self):
        runner = self.head  # a pointer to theh list's first head
        while(runner != None):   # iterarting while runner is a node and not None
            print(runner.value)   # print the current node's value
            runner = runner.next    # set the ruuner to it's neighbor
        return self     # once the loop is done return self to allow for chaining

    def add_to_back(self, val):     # accepts a value
        if self.head == None:       # if the list is empty
            self.add_to_front(val)      # run the add_ti_the_front method
            return self     # let's make sure the rest of the function doesn't happen if we add to the front
        new_node = SLNode(val)      # create a new instance of our Node class with the given value
        runner = self.head      # set an iterator to the start of the front list
        while(runner.next != None):     # iterator until the iterator doesn't have a neighbor
            runner = runner.next    # increment the runner to the next node in the list
        runner.next = new_node      # increment the runner to the next node in the list
        return self     # return self to allow for chaining

    def remove_from_front(self):
        if self.head != None:
            self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.head == None:
            return self
        elif self.head.next == None:
            self.head = None
            return self
        else:
            runner = self.head
            while ( runner.next.next != None ):
                runner = runner.next
            runner.next = None
        return self

# Testing our classes
my_list = SList()       # create a new instance of a list
my_list.add_to_front("Alejandro Fernandez").add_to_front("Hello, my name is").add_to_back("Nice to meet you").remove_from_back().print_values()