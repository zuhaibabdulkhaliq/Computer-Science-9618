# 2D Array: [Name, Code]
SubjectData = [
    ["CHEM", "9701"],
    ["CS", "9618"],
    ["FMT", "9231"],
    ["MTH", "9709"],
    ["PHY", "9702"]
]
NumberOfItems = len(SubjectData)

for Pointer in range(1, NumberOfItems):
    ItemToBeInserted = SubjectData[Pointer]
    CurrentItem = Pointer - 1
    
    while CurrentItem >= 0 and SubjectData[CurrentItem][1] > ItemToBeInserted[1]:
        SubjectData[CurrentItem + 1] = SubjectData[CurrentItem]
        CurrentItem = CurrentItem - 1
        
    SubjectData[CurrentItem + 1] = ItemToBeInserted

print("Sorted 2D Array (Insertion by Code):")
for row in SubjectData:
    print(row)