# Ecrire la procédure qui reçoit un tableau de taille N en entrée et qui réalise un tri par sélection

exemple = [1, 3, 5, 6, 3, 2, 4, 5, 6]


def triParSelection(tableau, n):
    for i in range(0, n):
        for j in range(i, n):
            if(tableau[i] > tableau[j]):
                min = tableau[j]
                tableau[j] = tableau[i]
                tableau[i] = min
    return tableau


print(triParSelection(exemple, 9))