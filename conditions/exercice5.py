# Ecrire un algorithme qui demande deux nombres à l’utilisateur et l’informe ensuite si le produit est négatif
# ou positif (on inclut cette fois le traitement du cas où le produit peut être nul. Attention, on ne doit pas calculer le produit.


def signe_produit():
    a = int(input("Veuillez saisir le nombre A \n"))
    b = int(input("Vuillez saisir le nombre  B \n"))

    if(a == 0 or b == 0):
        print("Le produit de vos deux nombres est 0")
    if(a > 0 and b > 0 or a < 0 and b < 0):
        print("Le produit de vos deux nombres est positif ")
    else:
        print("Le produit de vos deux nombres est négatif")


signe_produit()
