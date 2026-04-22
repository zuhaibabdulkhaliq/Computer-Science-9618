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
    if Tail == MAX_SIZE - 1: # Queue Full
        return False
    else:
        if Head == -1: # First item being added
            Head = 0
        Tail = Tail + 1
        MyList[Tail] = NewItem
        return True

def Dequeue():
    global Head, Tail, MyList
    if Head == -1 or Head > Tail:
        return "EMPTY"
    else:
        Temp = MyList[Head]
        Head = Head + 1
        return Temp