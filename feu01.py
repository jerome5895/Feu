# Definition de la fonction qui evalue une expression entre parentheses
def eval_parentheses(tokens):
    stack = []
    for token in tokens:
        if token == '(':
            stack.append(token)
        elif token == ')':
            expr = []
            while stack[-1] != '(':
                expr.append(stack.pop())
            stack.pop()
            stack.append(str(eval_expr(expr[::-1])))
        else:
            stack.append(token)
    return eval_expr(stack)

# Definition de la fonction qui evalue une expression
def eval_expr(tokens):
    operators = ['+', '-', '*', '/', '%']
    for operator in operators:
        for i in range(len(tokens)):
            if tokens[i] == operator:
                left = eval_expr(tokens[:i])
                right = eval_expr(tokens[i+1:])
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
    if len(tokens) == 1:
            return float(tokens[0])
    else:
        return eval_parentheses(tokens)
    
# Programme principal
if __name__ == '__main__':
    import sys
    tokens = sys.argv[1].split()
    print(eval_expr(tokens))