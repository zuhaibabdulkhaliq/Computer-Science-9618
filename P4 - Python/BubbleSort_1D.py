SubCode = ["9701", "9618", "9231", "9709", "9702"]
n = len(SubCode)


# --- METHOD 1: Using 2 For Loops (Less Efficient) ---
for i in range(n):

    for j in range(0, n - i - 1):
    
        if SubCode[j] > SubCode[j + 1]:
            temp = SubCode[j]
            SubCode[j] = SubCode[j + 1]
            SubCode[j + 1] = temp

print("Sorted 1D (2 For loops):", SubCode)



# --- METHOD 2: Using While & For Loop (Optimized) ---
SubCode = ["9701", "9618", "9231", "9709", "9702"]

Swap = True

while Swap == True:

    Swap = False

    for j in range(0, n - 1):
        if SubCode[j] > SubCode[j + 1]:
            temp = SubCode[j]
            SubCode[j] = SubCode[j + 1]
            SubCode[j + 1] = temp
            Swap = True

print("Sorted 1D (While & For):", SubCode)

# Pro Tip: In python you can swap also without using temp variable for e.g: a, b = b, a