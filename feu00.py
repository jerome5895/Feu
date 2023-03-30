import sys

# Function to print out a rectangle
def rectangle(C, L):
    for i in range(1, L+1):
        for j in range(1, C+1):
            if i == 1 or i == L or j == 1 or j == C:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

# Function to manage value and index errors
def try_except():
    try:
        C = int(sys.argv[1])
        L = int(sys.argv[2])
    except (ValueError, IndexError):
        print("Invalid input. Please provide two numbers.")
        sys.exit()
    return C, L

# Resolution
C, L = try_except()

# Print out result
rectangle(C, L)