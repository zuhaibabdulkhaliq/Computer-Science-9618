# Binary Search - The list MUST be sorted
MyList = ["CHEM", "CS", "FMT", "MTH", "PHY"] 

# --- ITERATIVE METHOD ---
def IterativeBinarySearch(SearchList, ValueToFind):
    Low = 0
    High = len(SearchList) - 1
    Location = -1

    while Low <= High and Location == -1:
        Mid = (Low + High) // 2
        
        if SearchList[Mid] == ValueToFind:
            Location = Mid
        elif SearchList[Mid] < ValueToFind:
            Low = Mid + 1
        else:
            High = Mid - 1
            
    return Location

# --- RECURSIVE METHOD ---
def RecursiveBinarySearch(SearchList, ValueToFind, Low, High):
    if Low > High:
        return -1 # Base Case: Value not found
    
    Mid = (Low + High) // 2
    
    if SearchList[Mid] == ValueToFind:
        return Mid # Base Case: Value found
    elif SearchList[Mid] < ValueToFind:
        # Recursive Step: Search Right half
        return RecursiveBinarySearch(SearchList, ValueToFind, Mid + 1, High)
    else:
        # Recursive Step: Search Left half
        return RecursiveBinarySearch(SearchList, ValueToFind, Low, Mid - 1)


SearchValue = input("Enter value to find: ")

# Iterative Test
Result1 = IterativeBinarySearch(MyList, SearchValue)
if Result1 != -1:
    print(f"Iterative Result: Found at {Result1}")
else:
    print("Value doesn't exists")

# Recursive Test
Result2 = RecursiveBinarySearch(MyList, SearchValue, 0, len(MyList) - 1)
if Result2 != -1:
    print(f"Iterative Result: Found at {Result2}")
else:
    print("Value doesn't exists")