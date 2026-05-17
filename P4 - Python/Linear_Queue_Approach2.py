# Global Variables
MAX_SIZE = 5
MyList = ["" for i in range(MAX_SIZE)]
Head = 0  # Points to the front of the queue
Tail = -1 # Points to the last item added
NumberOfItems = 0 # Tracks the current active size

def InitialiseQueue():
    global Head, Tail, NumberOfItems, MyList
    Head = 0
    Tail = -1
    NumberOfItems = 0
    for i in range(MAX_SIZE):
        MyList[i] = ""

def Enqueue(NewItem):
    global Tail, NumberOfItems, MyList
    
    # Check if Full: In a Linear Queue, it is full when the Tail hits the end of the array.
    # (Even if there is empty space at the front!)
    if Tail == MAX_SIZE - 1:
        return False
    else:
        Tail = Tail + 1
        MyList[Tail] = NewItem
        NumberOfItems = NumberOfItems + 1
        return True

def Dequeue():
    global Head, NumberOfItems, MyList
    
    # Check if Empty: Simplified by just checking our tracker
    if NumberOfItems == 0:
        return "EMPTY"
    else:
        Temp = MyList[Head]
        Head = Head + 1
        NumberOfItems = NumberOfItems - 1
        return Temp

# --- Testing the Queue ---
InitialiseQueue()

print("Enqueue CS:", Enqueue("CS"))     # Returns True
print("Enqueue MTH:", Enqueue("MTH"))   # Returns True

print("Dequeued:", Dequeue())           # Returns "CS"
print("Current Number of Items:", NumberOfItems) # Returns 1