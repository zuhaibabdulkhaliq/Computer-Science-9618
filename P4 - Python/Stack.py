# Global Variables
MAX_SIZE = 5
MyList = ["" for i in range(MAX_SIZE)]
TOS = -1  # -1 represents an empty stack

def InitialiseStack():
    global TOS, MyList
    TOS = -1
    for i in range(MAX_SIZE):
        MyList[i] = ""

def Push(NewItem):
    global TOS, MyList
    if TOS == MAX_SIZE - 1: # Stack Full
        return False
    else:
        TOS = TOS + 1
        MyList[TOS] = NewItem
        return True

def Pop():
    global TOS, MyList
    if TOS == -1: # Stack Empty
        return "EMPTY"
    else:
        Temp = MyList[TOS]
        MyList[TOS] = "" # Optional: clear the spot
        TOS = TOS - 1
        return Temp

# Example Test
InitialiseStack()
Push("A")
Push("B")
print("Popped:", Pop()) # Should be B