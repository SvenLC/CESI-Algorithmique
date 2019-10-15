# Ecrire un algorithme qui permet de calculer et d'afficher le prix TTC ainsi que le montant de TVA à partir d'un prix HT


def afficher_ttc():
    prixHT = int(input("Veuillez saisir votre prix HT"))
    prixTTC = calcul_ttc(prixHT)
    montantTVA = prixTTC - float(prixHT)
    print(prixTTC, " ", montantTVA)


def calcul_ttc(prixHT):
    tauxTVA = 1 + 20.6 / 100
    return prixHT * tauxTVA


afficher_ttc()
