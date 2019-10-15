# Ecrire un algorithme qui calcul le plus grand écart dans un tableau
# (l'écart est la valeur absolue de la différence de deux éléments)


exemple = [3, 4, 5, 1, 5, 6, 9, 7]


def calculMini(tableau):
    mini = tableau[0]
    for element in tableau:
        if(mini > element):
            mini = element
    return mini


def calculMaxi(tableau):
    maxi = tableau[0]
    for element in tableau:
        if(maxi < element):
            maxi = element
    return maxi


def calculEcart(tableau):
    return calculMaxi(tableau) - calculMini(tableau)


print(calculEcart(exemple))