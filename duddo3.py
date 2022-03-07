#Learning how a binary tree works, and how to go through it ( traverse it )
class Node:                             #making a blueprint for a node
    def __init__(self, key):            #constructor taking in a key / data as an argument
        self.val = key                  #value held by the object = key / data taken in by the constructor
        self.left = None                #left pointer of the object = none for now
        self.right = None               #Right pointer of the object = none for now

def travInOrder(root):              #function to traverse the binary tree in order
    if root:                        #if root exists ( let's say a recursive call to root.left happens, but there doesn't exist a left node to that root, then this case comes in handy)
        travInOrder(root.left)      #recursive call to traverse the left
        print(root.val)             #print the root
        travInOrder(root.right)     #recursive call to traverse the right

def travPostOrder(root):            #function to traverse the binary tree post order
    if root:                        #if root exists
        travPostOrder(root.left)    #recursive call to traverse the left
        travPostOrder(root.right)   #recursive call to traverse the right
        print(root.val)             #print the root

def travPreOrder(root):             #function to traverse the binary tree pre order
    if root:                        #if root exists
        print(root.val)             #print the root
        travPreOrder(root.left)     #recursive call to traverse the left
        travPreOrder(root.right)    #recursive call to traverse the right

#let's make a binary tree, then let's try to go through it ( traverse it )
root = Node(0)                          #Root =    0
root.left = Node(1)                     #L = 1          R = -1
root.right = Node(-1)               #L = 2   R = 3  #L = -2   R = -3
root.left.left = Node(2)                #############################
root.left.right = Node(3)               #       BINARY TREE         #
root.right.left = Node(-2)              #    REPRESENTED ABOVE      #
root.right.right = Node(-3)             #############################

travInOrder(root)
print('\n')
travPostOrder(root)
print('\n')
travPreOrder(root)
print('\n')
