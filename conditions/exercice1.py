# Ecrire un algorithme qui demande un nombre à l’utilisateur, et l’informe ensuite si ce nombre est positif ou négatif
# (on laisse de côté le cas où le nombre vaut 0).


def signe_nombre():
    nombre = int(input("Veuillez saisir un nombre \n"))
    if(nombre > 0):
        print("Votre nombre est positif")
    else:
        print("Votre nombre est négatif")


signe_nombre()
