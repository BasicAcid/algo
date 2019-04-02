#! /usr/bin/env python3

import random, argparse

parser = argparse.ArgumentParser(description='Binary tree')
parser.add_argument('-t', help='traverse the tree', action='store', dest='traverse_type')
args = parser.parse_args()

myList = []
LIST_LENGTH=9

def generate_list(n):
    """Generate random list"""
    myList.append(random.sample(range(1, 100), n))
    return myList[0]

# set value
myList = generate_list(LIST_LENGTH)

print("Initial list: %s\n" % myList)

class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """Insert data into tree"""
        if self.data:
            if data < self.data:
                if self.left is None:      # if node nonexistent
                    self.left = Node(data) # then create new node to left
                else:                      # else if node exists
                    self.left.insert(data) # then call algo with new value
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_inorder(self):
        """Print tree content inorder"""
        if self.left:
            self.left.print_inorder()
        print (self.data)
        if self.right:
            self.right.print_inorder()

    def print_postorder(self):
        """Print tree content postorder"""
        if self.right:
            self.right.print_postorder()
        print (self.data)
        if self.left:
            self.left.print_postorder()

    def print_outorder(self):
        """Print tree content out-order"""
        # Check if the current node is empty or null.
        # Traverse the right subtree by recursively calling the out-order function.
        # Display the data part of the root (or current node).
        # Traverse the left subtree by recursively calling the out-order function.
        if self.data:
            if self.right:
                self.right.print_outorder()
            print(self.data)
            if self.left:
                self.left.print_outorder()
        pass

    def print_preorder(self):
        """Print tree content preorder"""
        # Check if the current node is empty or null.
        # Display the data part of the root (or current node).
        # Traverse the left subtree by recursively calling the pre-order function.
        # Traverse the right subtree by recursively calling the pre-order function.
        if self.data:
            print(self.data)
            if self.left:
                self.left.print_preorder()
            if self.right:
                self.right.print_preorder()

def make_tree(lst):

    # Set Initial node
    root = Node(random.randint(1,100))

    # Fill it up !
    for i in lst:
        root.insert(i)
    return root

def nodes_distance(node, n1, n2):
    """
    Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca)
    'n1' and 'n2' are the two given keys
    'root' is root of given Binary Tree.
    'lca' is lowest common ancestor of n1 and n2
    Dist(n1, n2) is the distance between n1 and n2.
    """


# findMinMax(node, min, max, hd):
#      if node.data is None:
#          return

#      if hd is less than min then
#            min = hd;
#      else if hd is greater than max then
#           *max = hd;

#      findMinMax(tree->left, min, max, hd-1);
#      findMinMax(tree->right, min, max, hd+1);

def lca(root, n1, n2):
    """Find lowest common ancestor of n1 and n2"""
    if(root.data > n2 and root.data > n2):
        return lca(root.left, n1, n2)
    if(root.data < n2 and root.data < n2):
        return lca(root.right, n1, n2)
    return root

def o(n):
    """Time complexity"""
    # T(n) = T(k) + T(n – k – 1) + c
    pass

myTree = make_tree(myList)

#print(lca(myTree, myTree.left, myTree.right))

if args.traverse_type == "in":
    print("In-order traversal:")
    myTree.print_inorder()

elif args.traverse_type == "post":
    print("Post-order traversal:")
    myTree.print_postorder()

elif args.traverse_type == "pre":
    print("Pre-order traversal:")
    myTree.print_preorder()

elif args.traverse_type == "out":
    print("Out-order traversal:")
    myTree.print_outorder()
