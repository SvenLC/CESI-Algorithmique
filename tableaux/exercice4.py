# Ecrire l'algorithme permettant le calcul de la moyenne et du minimum des éléments d'un tableau

exemple = [3, 4, 5, 1, 5, 6, 9, 7]


def calcul_moyenne(tableau):
    total = 0
    for element in tableau:
        total += element

    return total / len(tableau)


def calcul_mini(tableau):
    mini = tableau[0]
    for element in tableau:
        if(mini > element):
            mini = element
    return mini


print(calcul_moyenne(exemple))
print(calcul_mini(exemple))
