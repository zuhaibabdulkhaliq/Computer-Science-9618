# A-Level 9618 Linked List Implementation
class List:
    def __init__(self):
        self.Data = ""
        self.Pointer = -1

# Global Variables
MAX_SIZE = 10
NULL_PTR = -1
MyList = [List() for i in range(MAX_SIZE)]
StartPtr = NULL_PTR
FreePtr = 0

def InitialiseList():
    global StartPtr, FreePtr
    StartPtr = NULL_PTR
    FreePtr = 0
    # Link all nodes into the free list
    for Index in range(0, MAX_SIZE - 1):
        MyList[Index].Pointer = Index + 1
    MyList[MAX_SIZE - 1].Pointer = NULL_PTR

def SearchList(Item):
    Found = False
    CurrentPtr = StartPtr
    
    # Traverse as long as the item isn't found and we haven't reached the end
    # Note: If the list is sorted, we can stop if MyList[CurrentPtr].Data > Item
    while Found == False and CurrentPtr != NULL_PTR:
        if Item == MyList[CurrentPtr].Data:
            Found = True
        else:
            CurrentPtr = MyList[CurrentPtr].Pointer
            
    if Found == True:
        print(f"Data '{Item}' found at index {CurrentPtr}")
    else:
        print(f"Data '{Item}' not found")
    return CurrentPtr

def InsertList(NewItem):
    global StartPtr, FreePtr
    
    if FreePtr == NULL_PTR:
        print("List is full")
    else:
        # 1. Take a node from the free list
        Temp = FreePtr
        FreePtr = MyList[FreePtr].Pointer
        MyList[Temp].Data = NewItem
        
        # 2. Check if inserting at the very beginning
        if StartPtr == NULL_PTR or NewItem < MyList[StartPtr].Data:
            MyList[Temp].Pointer = StartPtr
            StartPtr = Temp
        else:
            # 3. Traverse to find the correct sorted position
            CurrentPtr = StartPtr
            PreviousPtr = NULL_PTR
            
            while CurrentPtr != NULL_PTR and NewItem > MyList[CurrentPtr].Data:
                PreviousPtr = CurrentPtr
                CurrentPtr = MyList[CurrentPtr].Pointer
            
            # 4. Insert between PreviousPtr and CurrentPtr
            MyList[Temp].Pointer = CurrentPtr
            MyList[PreviousPtr].Pointer = Temp

def DeleteList(Item):
    global StartPtr, FreePtr
    
    Found = False
    CurrentPtr = StartPtr
    PreviousPtr = NULL_PTR
    
    # 1. Search for the item to delete
    while Found == False and CurrentPtr != NULL_PTR:
        if Item == MyList[CurrentPtr].Data:
            Found = True
        else:
            PreviousPtr = CurrentPtr
            CurrentPtr = MyList[CurrentPtr].Pointer
            
    if Found == True:
        # 2. If it's the first node, move StartPtr
        if CurrentPtr == StartPtr:
            StartPtr = MyList[CurrentPtr].Pointer
        else:
            # Bypass the current node
            MyList[PreviousPtr].Pointer = MyList[CurrentPtr].Pointer
            
        # 3. Return the deleted node to the Free List
        MyList[CurrentPtr].Pointer = FreePtr
        FreePtr = CurrentPtr
        print(f"Item '{Item}' deleted.")
    else:
        print(f"Item '{Item}' not found in list.")


InitialiseList()
InsertList("MTH")
InsertList("CS")
InsertList("PHY")
SearchList("CS")
DeleteList("CS")