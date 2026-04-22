SubName = ["CHEM", "CS", "FMT", "MTH", "PHY"]
SubCode = ["9701", "9618", "9231", "9709", "9702"]
n = len(SubCode)

# --- METHOD 1: Using 2 For Loops ---
Names1 = list(SubName)
Codes1 = list(SubCode)

for i in range(n):
    for j in range(0, n - i - 1):
        if Codes1[j] > Codes1[j + 1]:

            tempC = Codes1[j]
            Codes1[j] = Codes1[j + 1]
            Codes1[j + 1] = tempC

            tempN = Names1[j]
            Names1[j] = Names1[j + 1]
            Names1[j + 1] = tempN
            
print("Parallel Sorted (2 For):", Codes1, Names1)

# --- METHOD 2: Using While & For Loop ---
Names2 = list(SubName)
Codes2 = list(SubCode)

Swap = True

while Swap == True:

    Swap = False

    for j in range(0, n - 1):
        if Codes2[j] > Codes2[j + 1]:

            tempC = Codes2[j]
            Codes2[j] = Codes2[j + 1]
            Codes2[j + 1] = tempC

            tempN = Names2[j]
            Names2[j] = Names2[j + 1]
            Names2[j + 1] = tempN
            Swap = True

print("Parallel Sorted (While & For):", Codes2, Names2)