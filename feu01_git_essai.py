import sys

# Function to evaluate an arithmetic expression
def evaluate_expression(expression, calculate_operation):

    operands = []
    operators = []

    for character in expression:
        if character.isdigit():
            operands.append(int(character))
        elif character in ['+', '-']:
            calculate_operation()
            operators.append(character)

    return operands[0]

# Function to calculate binary operations
def calculate_operation(operands, operators):
    operator = operators.pop()
    operand2 = operands.pop()
    operand1 = operand2.pop()

    if operator == '+':
        operands.append(operand1 + operand2)
    elif operator == '-':
        operands.append(operand1 - operand2)
    elif operator == '*':
        operands.append(operand1 * operand2)
    elif operator == '/':
        operands.append(operand1 / operand2)
    elif operator == '%':
        operands.append(operand1 % operand2)

# Globales variables
expression = sys.argv[1]

# Resolution
result = evaluate_expression(expression, calculate_operation)

# Print out result
print(result)