# Ecrire un algorithme qui demande l’âge d’un enfant à l’utilisateur. Ensuite, il l’informe de sa catégorie


def categorie_enfant():
    age = int(input("Veuillez saisir l'age de l'enfant"))

    if(age >= 6 and age <= 7):
        print("Poussin")
    elif(age >= 8 and age <= 9):
        print("Pupille")
    elif(age >= 10 and age <= 11):
        print("Minime")
    elif(age >= 12):
        print("Cadet")
    else:
        print("Dans aucunes catégorie")
