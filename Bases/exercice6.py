# Écrire un algorithme qui permet d’échanger les valeurs de deux variables A et B, et ce quel que soit leur contenu préalable.


def transfert_valeur():
    a = int(input("Veuillez saisir A \n"))
    b = int(input("Veuillez saisir B \n"))

    d = b
    b = a
    a = d

    print("A = " + str(a))
    print("B = " + str(b))


transfert_valeur()
