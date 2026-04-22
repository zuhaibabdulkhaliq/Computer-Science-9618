# BASE CLASS (Parent) 
class Students:
    def __init__(self):
        self.__StudentID = "" # PRIVATE 
        self.__Name = ""
        self.__Age = 0

    # Setters and Getters 
    def SetDetails(self, i, n, a):
        self.__StudentID = i
        self.__Name = n
        self.__Age = a

    def GetName(self):
        return self.__Name
    
    def Display(self):
        # Using print statements for record viewing 
        print(f"ID: {self.__StudentID} | Name: {self.__Name} | Age: {self.__Age}")

# SUBCLASS (Child) - Inherits from Students 
class Subjects(Students):
    def __init__(self):
        # Call the parent constructor 
        super().__init__()
        self.__Marks = [0, 0, 0] # Representing sub1, sub2, sub3 
        
    def SetSubjects(self, s1, s2, s3):
        self.__Marks = [s1, s2, s3]

    # Method Overriding: Redefining Display for the child class 
    def Display(self):
        # super() allows us to run the parent's code first 
        super().Display()
        print(f"Marks: {self.__Marks[0]}, {self.__Marks[1]}, {self.__Marks[2]}")

# --- MANAGING AN ARRAY OF OBJECTS --- 

# 1. Declare Array of Objects using List Comprehension 
# This creates 3 UNIQUE instances of Subjects
myList = [Subjects() for index in range(3)]

# 2. Input Loop 
for i in range(3):
    print(f"\nEntering details for Student {i+1}:")
    id_val = input("ID: ")
    name_val = input("Name: ")
    age_val = int(input("Age: "))
    m1 = int(input("Mark 1: "))
    m2 = int(input("Mark 2: "))
    m3 = int(input("Mark 3: "))

    # Populate the object at the current index 
    myList[i].SetDetails(id_val, name_val, age_val)
    myList[i].SetSubjects(m1, m2, m3)

# 3. Output Loop (Polymorphism in action) 
print("\n--- STUDENT REPORT ---")
for student in myList:
    student.Display() # Calls the overridden Display() in Subjects