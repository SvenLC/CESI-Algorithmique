# Écrire un algorithme qui demande un nombre de départ, et qui ensuite affiche les dix nombres suivants.
# Par exemple, si l’utilisateur entre le nombre 17, le programme affichera les nombres de 18 à 27.
# Avec la boucle pour


def nombre_suivant():
    nombre = input(int('Veuillez saisir un nombre'))
    for i in range(0, 10):
        nombre += 1
        print(nombre)


nombre_suivant()
