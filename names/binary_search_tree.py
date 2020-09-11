# import time

# start_time = time.time()

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

from queue import Queue

from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if(value >= self.value):
            if(self.right == None):
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        elif(value < self.value):
            if(self.left == None):
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            self.value = value
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if(self.value == target):
            return True
        elif(target > self.value):
            if(self.right == None):
                return False
            elif(self.right.value == target):
                return True
            else:
                return self.right.contains(target)
        elif(target < self.value):
            if(self.left == None):
                return False
            elif(self.left.value == target):
                return True
            else:
                return self.left.contains(target)
        else:
            return False
        

    # Return the maximum value found in the tree
    def get_max(self):
        maximum = self.value
        while(maximum):
            if(self.value == None):
                return None
            elif(self.right):
                if(maximum <= self.value):
                    maximum = self.value
                return self.right.get_max()
            elif(self.right == None):
                return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if(self.left and self.right):
            self.left.for_each(fn)
            self.right.for_each(fn)
        if((self.left) and (self.right == None)):
            self.left.for_each(fn)
        if((self.right) and (self.left == None)):
            self.right.for_each(fn)
        fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if(self != None):
            if(self.left != None):
                self.left.in_order_print()
            print(self.value)
            if(self.right != None):
                self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
                # instantiate a queue
        q = Queue()
        v = list()
        # enqueue our starting node (self)
        q.enqueue(self)
        # while the queue is not empty
        while(q.size > 0):
            # dequeue the current node
            val = q.dequeue()
            v.append(val)
            
            # print the nodes value
            print(val.value)
            # check if left child exists
            if(val.left):
                # enqueue left child
                q.enqueue(val.left)

            # check if right child exists
            if(val.right):
                # enqueue right child
                q.enqueue(val.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
                # instantiate a stack
        s = Stack()
        v = list()
        # push our starting node (self)
        s.push(self)
        # while the stack is not empty
        while(s.size > 0):
            # pop the current node
            val = s.pop()
            v.append(val)
            
            # print the nodes value
            print(val.value)
            # check if left child exists
            if(val.left):
                # push left child
                s.push(val.left)

            # check if right child exists
            if(val.right):
                # push right child
                s.push(val.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        # instantiate a stack
        s = Stack()
        v = list()
        # push our starting node (self)
        s.push(self)
        # while the stack is not empty
        while(s.size > 0):
            # pop the current node
            val = s.pop()
            v.append(val)
            
            print(val.value)
            
            # check if right child exists
            if(val.right):
                # push right child
                s.push(val.right)

            # check if left child exists
            if(val.left):
                # push left child
                s.push(val.left)

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""

# duplicates = []

# bst = BSTNode(names_2[500])

# for i in names_2:
#     bst.insert(i)

# for j in names_1:
#     if(bst.contains(j)):
#         duplicates.append(j)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")