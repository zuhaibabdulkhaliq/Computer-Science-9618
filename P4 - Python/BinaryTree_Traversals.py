# Binary Tree Representation: [LeftPtr, Data, RightPtr]
# A value of -1 represents a Null Pointer
ArrayNodes = [
    [1, 11, 2],   # Index 0 (Root)
    [3, 2, 4],    # Index 1
    [-1, 13, -1], # Index 2
    [-1, 1, -1],  # Index 3
    [-1, 5, -1]   # Index 4
]
RootPointer = 0 # 

# --- 1. IN-ORDER TRAVERSAL ---
# Pattern: Left -> Root -> Right
# Use: Returns data in alphabetical or numerical order.
def InOrder(ArrayNodes, RootNode):
    # Check if a Left child exists
    if ArrayNodes[RootNode][0] != -1: 
        InOrder(ArrayNodes, ArrayNodes[RootNode][0]) [cite: 1]
    
    # Visit the Root (Print data)
    print(str(ArrayNodes[RootNode][1])) [cite: 1]
    
    # Check if a Right child exists
    if ArrayNodes[RootNode][2] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][2]) [cite: 1]

# --- 2. PRE-ORDER TRAVERSAL ---
# Pattern: Root -> Left -> Right
# Use: Often used to create a copy of the tree.
def PreOrder(ArrayNodes, RootNode):
    # Visit the Root (Print data) first
    print(str(ArrayNodes[RootNode][1])) [cite: 1]
    
    if ArrayNodes[RootNode][0] != -1:
        PreOrder(ArrayNodes, ArrayNodes[RootNode][0]) [cite: 1]
        
    if ArrayNodes[RootNode][2] != -1:
        PreOrder(ArrayNodes, ArrayNodes[RootNode][2]) [cite: 2]

# --- 3. POST-ORDER TRAVERSAL ---
# Pattern: Left -> Right -> Root
# Use: Used to delete a tree or evaluate postfix math expressions.
def PostOrder(ArrayNodes, RootNode):
    if ArrayNodes[RootNode][0] != -1:
        PostOrder(ArrayNodes, ArrayNodes[RootNode][0]) [cite: 1]
        
    if ArrayNodes[RootNode][2] != -1:
        PostOrder(ArrayNodes, ArrayNodes[RootNode][2]) [cite: 1]
        
    # Visit the Root last
    print(str(ArrayNodes[RootNode][1])) [cite: 1]

# Testing the Traversals
print("# Inorder Binary Tree Traversal")
InOrder(ArrayNodes, RootPointer)

print("\n# Preorder Binary Tree Traversal")
PreOrder(ArrayNodes, RootPointer)

print("\n# Postorder Binary Tree Traversal")
PostOrder(ArrayNodes, RootPointer)