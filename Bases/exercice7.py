# Écrire un algorithme qui permet d’échanger les valeurs de deux variables A et B, et ce quel que soit leur contenu préalable.


def transfert_nombre():
    a = int(input("Veuillez saisir A \n"))
    b = int(input("Veuillez saisir B \n"))
    c = int(input("Veuillez saisir C \n"))

    d = b
    b = a
    a = c
    c = d

    print("A = " + str(a))
    print("B = " + str(b))
    print("C = " + str(c))


transfert_nombre()
