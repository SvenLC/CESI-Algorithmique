# Écrire un algorithme qui demande un nombre de départ, et qui calcule la somme des entiers jusqu’à ce nombre,
# par exemple, si on entre 5, on devrait afficher 1 + 2 + 3 + 4 + 5.


def somme(nombre):
    total = 0
    for i in range(0, nombre):
        total = total + i
        print(i)

    return total


print(somme(10))
