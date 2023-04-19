# Function to evaluate an arithmetic expression
def evaluate(expression):
    operators = ['+', '-', '*', '/', '%']
    for operator in operators:
        for i in range(len(expression)):
            if expression[i] == operator:
                left = evaluate(expression[:i])
                right = evaluate(expression[i+1:])
                if operator == '+':
                    return left + right
                elif operator == '-':
                    return left - right
                elif operator == '*':
                    return left * right
                elif operator == '/':
                    return left / right
                elif operator == '%':
                    return left % right
    if len(expression) == 1:
        return int(expression[0])
    
# Main program
if __name__ == '__main__':
    import sys
    expression = sys.argv[1].split()
    print(evaluate(expression))