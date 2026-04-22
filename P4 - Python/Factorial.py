# --- ITERATIVE METHOD ---
def IterativeFactorial(n):
    Answer = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n + 1):
            Answer = Answer * i
        return Answer

# --- RECURSIVE METHOD ---
def RecursiveFactorial(n):
    if n == 0 or n == 1: 
        return 1 # Base Case
    else:
        # Recursive Step
        return n * RecursiveFactorial(n - 1)



Num = int(input("Enter a number to calculate factorial: "))

if Num < 0:
    print("Factorial does not exist for negative numbers")
else:
    print(f"Iterative Result: {IterativeFactorial(Num)}")
    print(f"Recursive Result: {RecursiveFactorial(Num)}")