MyList = ["CS", "MTH", "PHY", "FMT", "CHEM"]



# --- METHOD 1: Using For Loop ---
value_to_find = input("Enter the value to search: ")

location = -1
max_elements = len(MyList)

for index in range(max_elements):
    if MyList[index] == value_to_find:
        location = index
        break  # Exit the loop early once found

if location != -1:
    print(f"'{value_to_find}' found at index {location}")
else:
    print("Value does not exist!")
    


# --- METHOD 2: Using While Loop ---
value_to_find = input("Enter the value to search: ")

found = False
index = 0
max_elements = len(MyList)

while not found and index < max_elements:
    if MyList[index] == value_to_find:
        found = True
    else:
        index += 1

if found:
    print(f"'{value_to_find}' found at index {index}")
else:
    print("Value does not exist!")