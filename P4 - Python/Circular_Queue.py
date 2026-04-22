# Global Variables
MAX_SIZE = 5
MyList = ["" for i in range(MAX_SIZE)]
Head = -1
Tail = -1

def InitialiseQueue():
    global Head, Tail, MyList
    Head = -1
    Tail = -1
    for i in range(MAX_SIZE):
        MyList[i] = ""

def Enqueue(NewItem):
    global Head, Tail, MyList
    # Check if Full: (Head is at start and Tail at end) OR (Tail is right behind Head)
    if (Head == 0 and Tail == MAX_SIZE - 1) or (Head == Tail + 1):
        return False
    else:
        if Head == -1: # If Queue was empty
            Head = 0
            Tail = 0
        elif Tail == MAX_SIZE - 1: # Wrap around to the start
            Tail = 0
        else:
            Tail = Tail + 1
        
        MyList[Tail] = NewItem
        return True

def Dequeue():
    global Head, Tail, MyList
    if Head == -1: # Empty Check
        return "EMPTY"
    else:
        Temp = MyList[Head]
        
        if Head == Tail: # Last item removed, reset to empty state
            Head = -1
            Tail = -1
        elif Head == MAX_SIZE - 1: # Wrap around
            Head = 0
        else:
            Head = Head + 1
            
        return Temp


InitialiseQueue()
Enqueue("CS")
Enqueue("MTH")
print("Dequeued:", Dequeue())