# Ecrire un algorithme qui déclare et remplisse un tablea contenant les six voyelles de l'alphabet latin

voyelle = 'AEIOUY'

def remplirTableau():
    tableau = []
    for i in range(0, len(voyelle)):
        tableau.append(voyelle[i])    
    return tableau

print(remplirTableau())
