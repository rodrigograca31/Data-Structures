# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if new nodes value is less than out current nodes value
        if value < self.value:
            # if there is no left child already here
            if self.left == None:
                # place a new bst with the value passed in to the left
                self.left = BinarySearchTree(value)
            # otherwise
            else:
                # repeat the process recursively on the left
                self.left.insert(value)
        # else if the value is greater than or equal to the current nodes value
        else:
            # if there is no right child already here
            if self.right == None:
                # place a new bst with the value passed in to the right
                self.right = BinarySearchTree(value)
            # otherwise
            else:
                # repeat the process recursively on the right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base case. if value matches current target
        if self.value == target:
            # return True
            return True
        # if target less than value
        if target < self.value:
            # check left child recursively
            # if no left child
            if self.left == None:
                # return false
                return False
            # otherwise
            else:
                # call contains on the left
                return self.left.contains(target)
        # otherwise
        else:
            # check right child recursively
            # if no right child
            if self.right == None:
                # return false
                return False
            # otherwise
            else:
                # call contains on the right
                return self.right.contains(target)

        # return False

    # Return the maximum value found in the tree
    def get_max(self):
        while self.right:
            self = self.right

        return self.value

    # Return the minimum value found in the tree
    def get_min(self):
        while self.left:
            self = self.left

        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # do the call back using self.value as the parameter
        cb(self.value)

        # if left exists
        if self.left:
            # call foreach on left
            self.left.for_each(cb)

        # if right exists
        if self.right:
            # call foreach on right
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
