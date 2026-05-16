# 2D Array [Name, Code]
SubjectData = [
    ["CHEM", "9701"],
    ["CS", "9618"],
    ["FMT", "9231"],
    ["MTH", "9709"],
    ["PHY", "9702"]
]

n = len(SubjectData)

# --- METHOD 1: Using 2 For Loops ---
Data1 = [list(row) for row in SubjectData] # Create a copy

for i in range(n):

    for j in range(0, n - i - 1):
        if int(Data1[j][1]) > int(Data1[j + 1][1]):
            temp = Data1[j]
            Data1[j] = Data1[j + 1]
            Data1[j + 1] = temp

print("2D Sorted (2 For Loops):", Data1)

# --- METHOD 2: Using While & For Loop ---
Data2 = [list(row) for row in SubjectData]

Swap = True

while Swap == True:

    Swap = False

    for j in range(0, n - 1):
        if int(Data2[j][1]) > int(Data2[j + 1][1]):
            temp = Data2[j]
            Data2[j] = Data2[j + 1]
            Data2[j + 1] = temp
            Swap = True

print("2D Sorted (While & For):", Data2)

# Here we converted into integer when comparing values for sorting while setting ouur condition.
# But if the string length is same like in this case 4 & same for all elements
# We can compare values without conversion and it still works unless different lengths
# '9709' > '9231' but '9' < '11' may not work because not string lenghts are different
# Better to convert to integer for comparision
