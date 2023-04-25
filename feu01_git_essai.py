# Function to evaluate an arithmetic expression
def evaluate_expression(expression):

# Initialize stacks
    operands = []
    operators = []

# Function to calcul binary operation
    def calculate_operation():
        operator = operators.pop()
        operand2 = operands.pop()
        operand1 = operands.pop()

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

    # Make priority
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}

    for character in expression:
        if character.isdigit():
            operands.append(int(character))
        elif character in ['+', '-', '*', '/', '%']:
            while operators and operators[-1] != '(' and precedence[operators[-1]] >= precedence[character]:
                calculate_operation()
            operators.append(character)
        elif character == '(':
            operators.append(character)
        elif character == ')':
            while operators[-1] != '(':
                calculate_operation()
    while operators:
        calculate_operation()

    return operands[0]

# Globales variables
expression = sys.argv[1]

# Resolution
result = evaluate_expression(expression)

# Print out result
print(result)
