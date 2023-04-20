import sys

# Function to evaluate an arithmetic expression
def evaluer_expression(expression):
    operandes = []
    operateurs = []
    def calculer_operation():
        operateur = operateurs.pop()
        operande2 = operandes.pop()
        operande1 = operandes.pop()
        if operateur == '+':
            operandes.append(operande1 + operande2)
        elif operateur == '-':
            operandes.append(operande1 - operande2)
        elif operateur == '*':
            operandes.append(operande1 * operande2)
        elif operateur == '/':
            operandes.append(operande1 / operande2)
        elif operateur == '%':
            operandes.append(operande1 % operande2)
    for caractere in expression:
        if caractere.isdigit():
            operandes.append(int(caractere))
        elif caractere in ['+', '-', '*', '/', '%']:
            while operateurs and operateurs[-1] in ['*', '/']:
                calculer_operation()
            operateurs.append(caractere)
        elif caractere == '(':
            operateurs.append(caractere)
        elif caractere == ')':
            while operateurs[-1] != '(':
                calculer_operation()
            operateurs.pop()
    while operateurs:
        calculer_operation()
    return operandes[0]

# Globales variables
expression = sys.argv[1]

# Resolution
resultat = evaluer_expression(expression)

# Print out result
print(resultat)