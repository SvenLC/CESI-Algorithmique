# Ecrire un algorithme qui demande deux nombres à l’utilisateur et l’informe ensuite si leur produit est négatif ou positif
# (on laisse de côté le cas où le produit est null). Attention : on ne doit pas calculer le produit des deux nombres.


def signe_produit():
    a = int(input("Veuillez saisir le nombre A \n"))
    b = int(input("Vuillez saisir le nombre  B \n"))

    if(a > 0 and b > 0):
        print("Le produit de vos deux nombres est positif ")
    elif(a < 0 and b < 0):
        print("Le produit de vos deux nombres est positif")
    else:
        print("Le produit de vos deux nombres est négatif")


signe_produit()
