import sys

# Function to manage index errors
def areArgsValid(argArray):
    if len(argArray) != 3 or argArray[1] == 0 or argArray[2] == 0:
        return False
    else:
        return True

# Function to print out a rectangle
def rectangle(column, line):
    c = column
    l = line
    for i in range(1, l+1):
        for j in range(1, c+1):
            if i == 1 and j == 1 or i == 1 and j == c or i == l and j == 1 or i == l and j == c:
                print("o ", end="")
            elif i > 1 and i < l and j == 1 or i > 1 and i < l and j == c:
                print("| ", end="")
            elif j > 1 and j < c and i == 1 or j > 1 and j < c and i == l:
                print("- ", end="")
            else:
                print("  ", end="")
        print()

# Resolution and print out result
rectangle(int(sys.argv[1]), int(sys.argv[2])) if areArgsValid(sys.argv) == True else sys.exit("Invalid input. Please provide one number for length, and one number for width.")