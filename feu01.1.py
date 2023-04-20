import sys

# Definir une fonction pour evaluer une expression arithmetique
def evaluer_expression(expression):
    
    # Initialiser les piles pour les operandes et les operateurs
    operandes = []
    operateurs = []

    # Definir une fonction pour calculer les operations binaires
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
    
    # Analyser chaque caractere de l'expression arithmetique
    for caractere in expression:
        if caractere.isdigit():

            # Ajouter l'operande a la pile des operandes
            operandes.append(int(caractere))
        elif caractere in ['+', '-', '*', '/', '%']:

            # Traiter les operateurs de priorite superieure
            while operateurs and operateurs[-1] in ['*', '/']:
                calculer_operation()

            # Ajouter l'operateur a la pile des operateurs
            operateurs.append(caractere)
        elif caractere == '(':
            
            # Ajouter la parenthese ouvrante a la pile des operateurs
            operateurs.append(caractere)
        elif caractere == ')':

            # Traiter les operations jusqu'a la parenthese ouvrante correspondante
            while operateurs[-1] != '(':
                calculer_operation()

            # Supprimer la parenthese ouvrante de la pile des operateurs
            operateurs.pop()

    # Traiter les operations restantes
    while operateurs:
        calculer_operation()
    
    # Le resultat final est le seul element restant sur la pile des operandes
    return operandes[0]

# Variable globale
expression = sys.argv[1]

# Appeler la fonction evaluer_expression pour evaluer l'expression arithmetique
resultat = evaluer_expression(expression)

print(resultat)