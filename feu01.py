import sys

def evaluate(expression):
    try:
        return eval(expression)
    except(SyntaxError, ZeroDivisionError, NameError):
        print("Invalid input. The arithmetic expression is false.")
        exit()

expression = sys.argv[1]

result = evaluate(expression)
print("The result of your arithmetic expresssion is: ", result)