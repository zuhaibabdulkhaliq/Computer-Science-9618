class Tree:
    def __init__(self):
        self.Data = ""
        self.LeftPtr = -1
        self.RightPtr = -1

# Global Variables
NULL_PTR = -1
MyList = [Tree() for i in range(10)]
RootPtr = NULL_PTR
FreePtr = 0 # In Python, first free index is 0

def InitialiseTree():
    global RootPtr, FreePtr
    RootPtr = NULL_PTR
    FreePtr = 0
    # Link all nodes into the free list using the RightPtr
    for Index in range(0, 9):
        MyList[Index].RightPtr = Index + 1
    MyList[9].RightPtr = NULL_PTR

def SearchTree(Item):
    Found = False
    CurrentPtr = RootPtr
    
    while CurrentPtr != NULL_PTR and Found == False:
        if Item == MyList[CurrentPtr].Data:
            Found = True
        elif Item > MyList[CurrentPtr].Data:
            CurrentPtr = MyList[CurrentPtr].RightPtr
        else:
            CurrentPtr = MyList[CurrentPtr].LeftPtr
            
    if Found == True:
        print(f"Data found at index: {CurrentPtr}")
    else:
        print("Data not found")
    return CurrentPtr

def InsertTree(NewItem):
    global FreePtr, RootPtr
    
    if FreePtr == NULL_PTR:
        print("Tree is full")
    else:
        # 1. Grab a node from the free list
        Temp = FreePtr
        # Update FreePtr to the next available node
        FreePtr = MyList[FreePtr].RightPtr
        
        # 2. Initialize the new node
        MyList[Temp].Data = NewItem
        MyList[Temp].LeftPtr = NULL_PTR
        MyList[Temp].RightPtr = NULL_PTR
        
        # 3. If tree is empty, this node becomes the root
        if RootPtr == NULL_PTR:
            RootPtr = Temp
        else:
            CurrentPtr = RootPtr
            PreviousPtr = NULL_PTR
            TurnRight = False
            
            # 4. Traverse the tree to find the insertion point
            while CurrentPtr != NULL_PTR:
                PreviousPtr = CurrentPtr
                if NewItem > MyList[CurrentPtr].Data:
                    TurnRight = True
                    CurrentPtr = MyList[CurrentPtr].RightPtr
                else:
                    TurnRight = False
                    CurrentPtr = MyList[CurrentPtr].LeftPtr
            
            # 5. Connect the parent (PreviousPtr) to the new node (Temp)
            if TurnRight == True:
                MyList[PreviousPtr].RightPtr = Temp
            else:
                MyList[PreviousPtr].LeftPtr = Temp


InitialiseTree()
InsertTree("MTH")
InsertTree("CS")
InsertTree("PHY")
SearchTree("CS")