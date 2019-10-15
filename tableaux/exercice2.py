# Ecrire un algorithme qui déclare un tablea de 9 notes, dont on fait ensuite saisir les valeurs par l'utilisateur


def remplir_tableau():
    tableau = []
    for i in range(0, 9):
        tableau.append(
            input('Veuillez saisir la note n° ' + str(i + 1) + ' \n'))

    return tableau


print(remplir_tableau())
