# Ecrire un algorithme qui calcul le plus grand écart dans un tableau
# (l'écart est la valeur absolue de la différence de deux éléments)


exemple = [3, 4, 5, 1, 5, 6, 9, 7]


def calcul_mini(tableau):
    mini = tableau[0]
    for element in tableau:
        if(mini > element):
            mini = element
    return mini


def calcul_maxi(tableau):
    maxi = tableau[0]
    for element in tableau:
        if(maxi < element):
            maxi = element
    return maxi


def calcul_ecart(tableau):
    return calcul_maxi(tableau) - calcul_mini(tableau)


print(calcul_ecart(exemple))
