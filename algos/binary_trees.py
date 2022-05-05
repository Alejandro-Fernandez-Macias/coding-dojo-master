# Trees To Do 1

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root

# BST: Add
# Create an add(val) method on the BST object to add new value to the tree. This entails creating a BTNode with this value and connecting it at the appropriate place in the tree. Unless specified otherwise, BSTs can contain duplicate values.

    def add(self, data):
        runner = self.root
        #Create a node that contains a value or data
        new_node = Node(data)
        #Craete a while loop that stops when we get to the last node
        while runner:
        # Is the new data greater than or less than the current node
            if data > runner.data:
        # If there is another branch
                if runner.right:
                    runner = runner.right
                # If there is not a new branch, we add a branch
                else:
                    runner.right = new_node
                    return self
            else:
                if runner.left:
                    runner = runner.left
                else:
                    runner.left = new_node
                    return self
        return self

# BST: Contains
# Create a contains(val) method on BST that returns whether the tree contains a given value. Take advantage of the BST structure to make this a much more rapid operation than SList.contains() would be.

    def contains(self, data):
        runner = self.root
        while runner :
            if data > runner.data:
                runner = runner.right
            elif data < runner.data:
                runner = runner.left
            elif data == runner.data:
                return runner.data, "You have found the node you were looking for."
        return "Unfortunately these are not the nodes you are looking for"


# BST: Min
# Create a min() method on the BST class that returns the smallest value found in the BST.
    def find_min(data):
        runner = Node(data)
        while (runner.left is not None):
            runner = runner.left
        return runner.data , "-This is the minimun value of the BST"

# BST: Max
# Create a max() BST method that returns the largest value contained in the binary search tree.

    def find_max(root):
        runner = Node(root)
        while (runner.right):
            runner = runner.right
        return runner.data , "-This is the maximum value of the BST"

new_bst = BST(Node(13))

print(new_bst.root.data, "This is our Root")

new_bst.add(5).add(9).add(15).add(20).add(7).add(10).add(28)

print(new_bst.find_min())
print(new_bst.find_max())



