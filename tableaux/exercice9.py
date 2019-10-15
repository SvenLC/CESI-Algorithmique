# A partir d'une grille donnée, écrivez la fonction qui indique si un sudoku est gagnant ou pas
# (ie, tous les nombres de 1 à 9 apparaissent une fois sur la ligne et sur la colonne)

sudoku = [
    [7,1,3,8,2,4,6,5,9],
    [2,6,9,1,7,5,3,8,4],
    [5,4,8,6,9,3,2,1,7],
    [6,9,1,2,4,8,5,7,3],
    [4,7,2,3,5,1,9,6,8],
    [3,8,5,9,6,7,4,2,1],
    [1,3,4,5,8,2,7,9,6],
    [9,5,7,4,1,6,8,3,2],
    [8,2,6,7,3,9,1,4,5]]

def rechercher_valeur(tableau, valeur):
    double = False
    occurence = 0

    for i in range(0, len(tableau)):
        if(tableau[i] == valeur):
            occurence += 1

    if(occurence > 1):
        double = True

    return double

def tester_tableau(tableau):
    estValide = True
    for i in range(0, 9):
        if(rechercher_valeur(tableau, i)):
            estValide = False
    return estValide

def colonne_to_tableau(grille, index):
    tableau = []
    for i in range(0, len(grille)):
        tableau.append(grille[i][index])
    return tableau
    
def tester_sudoku(sudoku):
    estValide = True
    for i in range(0,9):
        if(not tester_tableau(sudoku[i])):
            estValide = False

    for i in range(0,9):
        tableau = colonne_to_tableau(sudoku, i)
        if(not tester_tableau(tableau)):
            estValide = False



    return estValide
    
print(tester_sudoku(sudoku))