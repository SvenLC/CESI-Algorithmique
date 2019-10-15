# Écrire un algorithme qui demande un nombre compris entre 10 et 20, jusqu’à ce que la réponse convienne.
# En cas de réponse supérieure à 20, on fera apparaitre un message « Plus petit ! », et inversement, « Plus grand ! »
# s’il est inférieur à 10.


def nombre_entre_10_et_20():
    nb = 0

    while (nb < 10 or nb > 20):
        nb = int(input("Veuillez saisir un nombre entre 1 et 3"))
        if(nb > 20):
            print("Veuillez écrire un nombre plus petit")
        elif(nb < 10):
            ("Veuillez écrire un nombre plus grand")
