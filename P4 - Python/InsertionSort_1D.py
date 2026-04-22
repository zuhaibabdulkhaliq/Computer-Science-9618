SubCode = ["9701", "9618", "9231", "9709", "9702"]
NumberOfItems = len(SubCode)

# We start from index 1 (the second item)
for Pointer in range(1, NumberOfItems):

    ItemToBeInserted = SubCode[Pointer]
    CurrentItem = Pointer - 1
    
    while CurrentItem >= 0 and SubCode[CurrentItem] > ItemToBeInserted:
        SubCode[CurrentItem + 1] = SubCode[CurrentItem]
        CurrentItem = CurrentItem - 1
        
    SubCode[CurrentItem + 1] = ItemToBeInserted

print("Sorted 1D Array (Insertion):", SubCode)