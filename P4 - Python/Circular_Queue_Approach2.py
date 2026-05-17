# Global Variables
MAX_SIZE = 5
MyList = ["" for i in range(MAX_SIZE)]
Head = 0  # Points to the front of the queue
Tail = -1 # Points to the last item added
NumberOfItems = 0 # Tracks the current size

def InitialiseQueue():
    global Head, Tail, NumberOfItems, MyList
    Head = 0
    Tail = -1
    NumberOfItems = 0
    for i in range(MAX_SIZE):
        MyList[i] = ""

def Enqueue(NewItem):
    global Tail, NumberOfItems, MyList
    
    # 1. Check if Full using NumberOfItems
    if NumberOfItems == MAX_SIZE:
        return False
    else:
        # 2. Increment Tail, wrapping around to 0 if it hits the end
        if Tail == MAX_SIZE - 1:
            Tail = 0
        else:
            Tail = Tail + 1
        
        # 3. Insert item and increment tracker
        MyList[Tail] = NewItem
        NumberOfItems = NumberOfItems + 1
        return True

def Dequeue():
    global Head, NumberOfItems, MyList
    
    # 1. Check if Empty using NumberOfItems
    if NumberOfItems == 0:
        return "EMPTY"
    else:
        # 2. Store the item to be dequeued
        Temp = MyList[Head]
        
        # 3. Increment Head, wrapping around to 0 if it hits the end
        if Head == MAX_SIZE - 1:
            Head = 0
        else:
            Head = Head + 1
            
        # 4. Decrement tracker and return item
        NumberOfItems = NumberOfItems - 1
        return Temp

# --- Testing the Queue ---
InitialiseQueue()

print("Enqueue CS:", Enqueue("CS"))     # Returns True
print("Enqueue MTH:", Enqueue("MTH"))   # Returns True

print("Dequeued:", Dequeue())           # Returns "CS"
print("Current Number of Items:", NumberOfItems) # Returns 1