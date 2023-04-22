import sys

# Function to evaluate an arithmetic expression
def evaluate_expression(expression):

    operands = []
    operators = []

    def calculate_operation():
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

    for character in expression:
        if character.isdigit():
            operands.append(int(character))
        elif character in ['+', '-']:
            calculate_operation()
            operators.append(character)

    return operands[0]

expression = sys.argv[1]

result = evaluate_expression(expression)

print(result)