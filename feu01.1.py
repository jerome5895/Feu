import sys

expression = sys.argv[1]

def evaluate(expr):
    operators = ['+', '-', '*', '/', '%']
    for operator in operators:
        for i in range(expr + 1):
            if i == operator:
                
