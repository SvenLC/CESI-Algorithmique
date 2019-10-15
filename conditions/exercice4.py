# Ecrire un algorithme qui demande un nombre à l’utilisateur et l’informe ensuite si ce nombre est positif ou négatif
# (on inclut cette fois le traitement du cas où le nombre vaut zéro)


def signe_nombre():
    nombre = int(input("Veuillez saisir un nombre \n"))
    if(nombre > 0):
        print("Votre nombre est positif")
    elif(nombre < 0):
        print("Votre nombre est négatif")
    else:
        print("Votre nombre est 0")


signe_nombre()
