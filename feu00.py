import sys

C = int(sys.argv[1])
L = int(sys.argv[2])

def rectangle():
    for i in range(1, L+1):
        for j in range(1, C+1):
            if i == 1 or i == L or j == 1 or j == C:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

rectangle()