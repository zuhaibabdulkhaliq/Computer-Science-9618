# In Python, a Record is implemented as a Class
class Students:
    def __init__(self):
        # Initializing fields(public) with default values
        self.StudentID = ""  # STRING
        self.Name = ""       # STRING
        self.Age = 0         # INTEGER
        self.Gender = ""     # CHAR (In Python, this is just a string)

        # For Private Variable just add __
        # self.__Gender = ""

# --- Performing operations with a single variable ---

# Declaring a variable of our defined datatype
MyStudent = Students()

# Assigning values
MyStudent.Name = "Ali"
MyStudent.StudentID = "MR1001"
MyStudent.Age = 17
MyStudent.Gender = "M"

# --- Working with an Array of Records ---

# Declaring an array of 10 Students
# We use a list comprehension to create 10 separate student objects
MyData = [Students() for i in range(10)]

# Accessing 5th element and storing name there
# Remember: Pseudocode index 5 is Python index 4
MyData[4].Name = "Zuhaib"

# Copying data from 5th element to 8th element
# Pseudocode index 8 is Python index 7
MyData[7].Name = MyData[4].Name

# --- Printing to verify ---
print(f"Single Student: {MyStudent.Name}, {MyStudent.StudentID}")
print(f"Student at Index 4: {MyData[4].Name}")
print(f"Student at Index 7 (copied): {MyData[7].Name}")