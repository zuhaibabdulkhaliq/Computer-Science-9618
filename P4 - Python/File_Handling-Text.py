# --- TEXT FILE HANDLING: SEQUENTIAL RECORDS ---
FILENAME = "Alpha25.txt"

def AddRecords():
    """Adds a validated record to the text file in append mode."""
    # Append mode 'a' will create the file if it doesn't exist 
    try:
        myFile = open(FILENAME, "a")

        # 1. Input & Validation: Student ID (Length check) 
        studentID = input("Enter StudentID (6 characters): ").upper()
        while len(studentID) != 6:
            studentID = input("Invalid, please re-enter (6 chars): ").upper()    

        # 2. Input & Validation: Name (Check if empty) 
        name = input("Enter Name: ").upper()
        while name == "":
            name = input("Please enter name: ").upper()

        # 3. Input & Validation: Age (Range check) 
        age = int(input("Enter Age (15-20): "))
        while age < 15 or age > 20:
            age = int(input("Invalid, please re-enter: "))

        # 4. Input & Validation: Gender (Choice check) 
        gender = input("Enter Gender (M/F): ").upper()
        while gender != "M" and gender != "F":
            gender = input("Invalid, please re-enter: ").upper()

        # Format record as one line: "ID NAME AGE GENDER\n" 
        info = studentID + " " + name + " " + str(age) + " " + gender + "\n"
        myFile.write(info)
        myFile.close()
        print("Record saved successfully.")
    except IOError:
        print("Error: Could not write to file.")

def DisplayRecords():
    """Reads lines and splits them into individual variables."""
    print("\n--- Current Text Records ---")
    try:
        myFile = open(FILENAME, "r")
        # Read first line and strip newline 
        info = myFile.readline().strip() 
        
        while info != "":
            # Split the string by whitespace into variables 
            studentID, name, age, gender = info.split()
            print(f"ID: {studentID} | Name: {name} | Age: {age} | Gender: {gender}")
            
            # Read next line 
            info = myFile.readline().strip()

        myFile.close()
    except FileNotFoundError:
        print("Error: File not found.")
    print("----------------------------\n")

# Testing
AddRecords()
DisplayRecords()