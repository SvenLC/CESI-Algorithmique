# Ecrire un algorithme qui déclare et remplisse un tableau de 7 valeurs
# numériques en les mettants toutes à zéro

def creerTableau():
    tableau = []
    for i in range (0,6):
        tableau.append(0)

    return tableau

print(creerTableau())