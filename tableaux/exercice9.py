# A partir d'une grille donnée, écrivez la fonction qui indique si un sudoku est gagnant ou pas
# (ie, tous les nombres de 1 à 9 apparaissent une fois sur la ligne et sur la colonne)

# La résolution ci dessous se fait de manière naive en testant à successivement les lignes, les colonnes et les blocs

sudokuValide = [
    [7, 1, 3, 8, 2, 4, 6, 5, 9],
    [2, 6, 9, 1, 7, 5, 3, 8, 4],
    [5, 4, 8, 6, 9, 3, 2, 1, 7],
    [6, 9, 1, 2, 4, 8, 5, 7, 3],
    [4, 7, 2, 3, 5, 1, 9, 6, 8],
    [3, 8, 5, 9, 6, 7, 4, 2, 1],
    [1, 3, 4, 5, 8, 2, 7, 9, 6],
    [9, 5, 7, 4, 1, 6, 8, 3, 2],
    [8, 2, 6, 7, 3, 9, 1, 4, 5]]

sudokuFaux = [
    [1, 1, 3, 8, 2, 4, 6, 5, 9],
    [2, 6, 9, 1, 7, 5, 3, 8, 4],
    [5, 4, 8, 6, 9, 3, 2, 1, 7],
    [6, 9, 1, 2, 4, 8, 5, 7, 3],
    [4, 7, 2, 3, 5, 1, 9, 6, 8],
    [3, 8, 5, 9, 6, 7, 4, 2, 1],
    [1, 3, 4, 5, 8, 2, 7, 9, 6],
    [9, 5, 7, 4, 1, 6, 8, 3, 2],
    [8, 2, 6, 7, 3, 9, 1, 4, 5]]


def rechercher_valeur(tableau, valeur):
    double = False
    occurence = 0
    i = 0

    while(i < 9 and occurence < 2):
        if(tableau[i] == valeur):
            occurence += 1
        i += 1
    if(occurence > 1):
        double = True

    return double


def tester_tableau(tableau):
    estValide = True
    i = 0
    while(estValide and i < 9):
        if(rechercher_valeur(tableau, i)):
            estValide = False
        i += 1
    return estValide


def colonne_to_tableau(grille, index):
    tableau = []
    for i in range(0, len(grille)):
        tableau.append(grille[i][index])
    return tableau


def bloc_to_tableau(grille, x, y):
    tableau = []
    for i in range(x, x+3):
        j = y
        for j in range(y, y+3):
            tableau.append(grille[i][j])
    return tableau


def tester_ligne(grille):
    estValide = True
    i  = 0
    while(estValide and i < 9):
        if(not tester_tableau(grille[i])):
            estValide = False
        i += 1
    return estValide


def tester_colonne(grille):
    estValide = True
    i = 0
    while(estValide and i < 9):
        tableau = colonne_to_tableau(grille, i)
        if(not tester_tableau(tableau)):
            estValide = False
        i += 1
    return estValide


def tester_bloc(grille):
    estValide = True
    i = 0
    while(estValide and i < 9):
        j = 0
        while(estValide and j < 9):
            tableau = bloc_to_tableau(grille, i, j)
            if(not tester_tableau(tableau)):
                estValide = False
            j += 3
        i += 3
    return estValide


def tester_sudoku(sudoku):
    estValide = True
    if(not tester_ligne(sudoku)):
        estValide = False
    elif(not tester_colonne(sudoku)):
        estValide = False
    elif(not tester_bloc(sudoku)):
        estValide = False

    return estValide


print(tester_sudoku(sudokuValide))
