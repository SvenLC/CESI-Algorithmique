# Ecrivez un algorithme permettant, toujours sur le même principe, à l'utilisateur de saisir un nombre déterminé de valeurs.
# Le Programme, une fois la saisie terminée, renvoie la plus grande valeur en précisant quelle position elle occupe dans
# le tableau. On prendra soin d'effectuer la saisie dans une premier temps, et la recherche de la plus grande valeur du
# tableau dans un deuxième temps


def saisir_tableau(taille):
    tableau = []
    for i in range(0, taille):
        tableau.append(
            int(input('Veuillez saisir un nombre à ajouter dans votre tableau \n')))
    return tableau


def recherche_index_max(tableau):
    max = tableau[0]
    index = 0
    for i in range(0, len(tableau)):
        if(max < tableau[i]):
            max = tableau[i]
            index = i

    return index


def initialisation_tableau():
    taille = int(input('Veuillez saisir la taille de votre tableau \n'))
    print('Remplissez le tableau')
    tableau = saisir_tableau(taille)
    print('Votre tableau est : ' + str(tableau))
    index = recherche_index_max(tableau)
    print('La plus grande valeur de votre tablea est à l\'index ' +
          str(index) + ' et sa valeur est ' + str(tableau[index]))


initialisation_tableau()
