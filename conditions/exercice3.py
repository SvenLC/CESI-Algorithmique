# Ecrire un algorithme qui demande trois noms à l’utilisateur et l’informe ensuite s’ils
# sont rangés ou non dans l’ordre alphabétique


def est_trie():
    a = input("Veuillez saisir le nom A \n")
    b = input("Vuillez saisir le nom  B \n")
    c = input("Vuillez saisir le nom  C \n")

    A = ord(a[0].upper())
    B = ord(b[0].upper())
    C = ord(c[0].upper())

    if(A <= B and B <= C):
        print("Les nom sont rangés par ordre alphabétique")
    else:
        print("Les nom ne sont pas rangés par odre alphabétique")


est_trie()
