# Ecrire un algorithme qui demande à l'utilisateur de saisir des nombres jusqu'a ce que la somme de ces nombre atteigne un plafond
# déterminé


def somme_jusqua(plafond):
    total = 0
    nb = 0
    while(total < plafond):
        nb = int(input("Veuillez saisir un nombre \n"))
        total += nb

    return total


print(somme_jusqua(10))
