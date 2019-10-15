# Ecrivez un algorithme constituant un tableau, à partir de deux tableaux de même longueur préalablement saisis.
# Le nouveau tableau sera la somme des éléments des deux tableaux de départ.

def somme_tableau(tableau1, tableau2):
    tableau3 = []
    for i in range (0,len(tableau1)):
        tableau3.append(tableau1[i] + tableau2[i])

    return tableau3

def saisir_tableau(taille):
    tableau = []
    for i in range (0, taille):
        tableau.append(int(input('Veuillez saisir un nombre à ajouter dans votre tableau \n')))
    return tableau

    
def initialisation_tableau():
    taille = int(input('Veuillez saisir la taille de votre tableau \n'))
    print('Remplissez le tableau n°1')
    tableau1 = saisir_tableau(taille)
    print('Votre tableau n°1 est : ' + str(tableau1))
    print('Remplissez le tableau n°2')
    tableau2 = saisir_tableau(taille)
    print('Votre tableau n°2 est : ' + str(tableau2))

    print('La somme des tableaux est : ' + str(somme_tableau(tableau1, tableau2)))

initialisation_tableau()