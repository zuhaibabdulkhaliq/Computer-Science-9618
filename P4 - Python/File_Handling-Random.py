import pickle

# 1. Record Definition 
class Students:
    def __init__(self):
        self.StudentID = 0  # INTEGER
        self.Name = ""       # STRING
        self.Age = 0        # INTEGER
        self.Gender = ""    # CHAR

# 2. Global Configurations 
FILENAME = "MyData.dat"
MAX_RECORDS = 10

def Hash(ID):
    """Hashing Algorithm: ID MOD Max_Records """
    return ID % MAX_RECORDS

def InitialiseFile():
    """Pre-fills file with empty records to reserve space."""
    EmptyList = [Students() for i in range(MAX_RECORDS)]
    try:
        with open(FILENAME, "wb") as File:
            pickle.dump(EmptyList, File)
        print("Random access file initialised.")
    except IOError:
        print("Error creating file.")

def AddRecord():
    """Hashes the ID and saves the record at the specific index."""
    try:
        # Load the whole array into memory 
        with open(FILENAME, "rb") as File:
            MyData = pickle.load(File)
        
        NewStudent = Students()
        NewStudent.StudentID = int(input("Enter Student ID: "))
        NewStudent.Name = input("Enter Name: ")
        NewStudent.Age = int(input("Enter Age: "))
        NewStudent.Gender = input("Enter Gender: ")

        # Calculate location using Hashing 
        Index = Hash(NewStudent.StudentID)
        
        # PUTRECORD: Replace the empty object at that index 
        MyData[Index] = NewStudent

        # Save the updated list back to the file 
        with open(FILENAME, "wb") as File:
            pickle.dump(MyData, File)
        print(f"Record stored at index {Index}.")
    except (IOError, ValueError):
        print("Error: Invalid input or file error.")

def SearchRecord(SearchID):
    """Calculates hash and retrieves record at that index."""
    try:
        with open(FILENAME, "rb") as File:
            MyData = pickle.load(File)

        Index = Hash(SearchID) # Calculate the address 
        Result = MyData[Index] # GETRECORD logic 

        # Verify the ID matches (check for empty slot) 
        if Result.StudentID == SearchID:
            print("\n--- Record Found ---")
            print(f"ID: {Result.StudentID} | Name: {Result.Name} | Age: {Result.Age}")
        else:
            print("Record not found (Slot empty or collision).")
    except (FileNotFoundError, IOError):
        print("Error: Could not open binary file.")

# Testing
InitialiseFile()
AddRecord()
search_id = int(input("\nEnter ID to find: "))
SearchRecord(search_id)