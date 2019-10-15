# Ecrire l'algorithme permettant le calcul du nombre d'occurence d'un élément donnée dans un tableau

exemple = [3, 4, 5, 1, 5, 6, 9, 7]


def calcul_nombre_occurence(valeur, tableau):
    compteur = 0
    for i in range(0, len(tableau)):
        if(tableau[i] == valeur):
            compteur += 1

    return compteur


print(calcul_nombre_occurence(4, exemple))
