import sys

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

# Function to manage value and index errors
def try_except():
    try:
        column = int(sys.argv[1])
        line = int(sys.argv[2])
    except (ValueError, IndexError):
        print("Invalid input. Please provide two numbers.")
        sys.exit()
    return column, line

# Resolution
column, line = try_except()

# Print out result
rectangle(column, line)