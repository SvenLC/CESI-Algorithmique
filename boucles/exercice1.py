# Ecrire un algorithme demande à l’utilisateur un nombre compris entre 1 et 3 jusqu’à ce que la réponse convienne.


def nombre_entre_1_et_3():
    nb = 0
    while (nb < 1 or nb > 3):
        nb = int(input("Veuillez saisir un nombre entre 1 et 3"))


nombre_entre_1_et_3()
