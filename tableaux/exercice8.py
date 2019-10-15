# Ecrivez un algo remplissant un tableau de 6 sur 13, avec des zéros


def remplir_tableau(longeur, largeur):
    tableau = []
    for i in range(0, longeur):
        tableau.append([])
        print(tableau)
        for y in range(0, largeur):
            tableau[i].append(0)

    return tableau


print(remplir_tableau(6, 13))
