# --- EXAMPLE 1: ZeroDivisionError ---
# This handles the logic error of dividing a number by zero.
def calculate_average(total_score, num_players):
    try:
        average = total_score / num_players
        print(f"Average Score: {average}")
    except ZeroDivisionError:
        # This block runs only if num_players is 0
        print("Error: Division by zero is not allowed.")


# --- EXAMPLE 2: File Access Errors (FileNotFoundError / IOError) ---
# Essential for protecting programs that interact with external storage.
def read_data_file(filename):
    try:
        # Attempt to open the file for reading 
        file = open(filename, "r")
        content = file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        # Specifically catches when the filename does not exist 
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        # Catches general input/output failures 
        print("Error: An issue occurred while accessing the disk.")


# --- EXAMPLE 3: ValueError ---
# Used when a function receives a value of the correct type but invalid content.
# Common when converting user input to integers for record storage.
def get_valid_age():
    try:
        # This will raise a ValueError if the user enters letters instead of numbers
        age = int(input("Enter Student Age: "))
        print(f"Age set to: {age}")
    except ValueError:
        # Catches conversion errors during int() casting 
        print("Error: Invalid input. Please enter a numerical value.")


# --- Practical Application Loop ---
# Combining multiple exceptions
def robust_input_example():
    try:
        number = int(input("Enter a number to divide 100 by: "))
        result = 100 / number
        print(f"Result: {result}")
    except (ValueError, ZeroDivisionError):
        # You can group multiple errors into a single tuple
        print("Error: You must enter a number that is not zero.")

# --- Testing the Functions ---
print("Testing ZeroDivision:")
calculate_average(500, 0)

print("\nTesting FileError:")
read_data_file("missing_notes.txt")

print("\nTesting ValueError:")
get_valid_age()