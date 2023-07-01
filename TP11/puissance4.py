from os import system

grids = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
]



def print_grid(grids: list[list[str]]):
    """Fonction chargée d'afficher la grille"""

    patterns = [['+---+', 0], ['---+', 1], ['---+', 2], ['---+', 3], ['---+', 4], ['---+', 5], ['---+', 6]]
    print()
    for i in range(6):
        for j in range(7):
            if j == 6:
                print(f"| {grids[i][j]} |", end="   ")
            else: 
                print(f"|{grids[i][j]}", end="  ")
        if i == 5:
            print()
        else:
            print('\n')
    for i in range(2):
        for j in range(7):
            if i == 1:
                print(f"  {patterns[j][i]}", end= " ")
            else:
                print(f"{patterns[j][i]}", end="")
        print()

# print_grid(grids)

def get_player(player_number: int) -> str:
    """Fonction permettant d'assigner un caractère à un joueur"""
    if player_number == 1:
        return 'O'
    else:
        return 'X'

def column_choosing(grid: list[list[str]], player_number: int) -> int:
    """Fonction permettant à un joueur de choisir une colonne"""

    try:
        print_grid(grids)
        player_character = get_player(player_number)
        print("Choisissez une colonne")
        column = int(input(f"Joueur {player_number} caractère {player_character} : "))
        if column in range(7):
            for i in range(5, -1, -1):
                if grid[i][column] not in ('X', 'O'): 
                    grid[i][column] = player_character
                    break
            return column
        elif column == -1:
            pass
        else:
            print("Cette colonne n'existe")
            pass
        return -1
    except:
        print("Valeur non valide")
        return -1

def check_horizontal_win(grids: list[list[str]], column: int) -> bool:
    """Fonction  qui d´etermine si le dernier pion joué fait partie
    d’un alignement horizontal de 4 pions consécutifs appartenant à un
    même joueur"""

    state = False
    count = 0
    for grid in grids:
        count = 0
        for i in range(column + 1, column + 4):
            if column == 6 or i > 6:
                break
            if grid[column] == grid[i] and grid[column] in ('X', 'O'):
                count += 1
            else:
                break
        for i in range(column - 1, column - 4, -1):
            if column == 0 or i < 0:
                break
            if grid[column] == grid[i] and grid[column] in ('X', 'O'):
                count += 1
            else:
                break
        if count == 3:
            state = True
            break
        else:
            count = 0

    return state

def check_vertical_win(grids: list[list[str]], column: int) -> bool:
    """Fonction  qui d´etermine si le dernier pion joué fait partie
    d’un alignement vertical de 4 pions consécutifs appartenant à un
    même joueur"""

    state = False
    count = 0
    for i in range(5):
        if grids[i][column] == grids[i + 1][column] and grids[i][column] in ('X', 'O'):
            count += 1
        else:
            count = 0
        if count == 3:
            state = True
            break

    return state

def check_top_left_win(grids: list[list[str]], column: int) -> bool:
    """Fonction  qui détermine si le dernier pion joué fait partie
    d’un alignement sur une diagonale (orientée de en haut à gauche 
    à enbas à droite)de 4 pions consécutifs appartenant à un
    même joueur"""

    state = False
    count = 1
    initial_column = column
    if column < 6:
        for i in range(0, 5):
            if grids[i][column] == grids[i + 1][column + 1] and grids[i][column] in ('X', 'O'):
                count += 1
                column += 1

    column = initial_column
    for i in range(5, -1, -1):
        if grids[i][column] == grids[i - 1][column - 1] and grids[i][column] in ('X', 'O'):
            count += 1
            column -= 1

    if count == 4:
        state = True

    return state

def check_top_rigth_win(grids: list[list[str]], column: int) -> bool:
    """Fonction  qui d´etermine si le dernier pion joué fait partie
    d’un alignement sur une diagonale (orientée de en haut à gauche 
    à enbas à droite)de 4 pions consécutifs appartenant à un
    même joueur"""

    state = False
    count = 1
    initial_column = column

    for i in range(0, 5):
        if grids[i][column] == grids[i + 1][column - 1] and grids[i][column] in ('X', 'O'):
            count += 1
            column -= 1

    column = initial_column
    if column < 6:
        column = initial_column
        for i in range(5, 0, -1):
            if grids[i][column] == grids[i - 1][column + 1] and grids[i][column] in ('X', 'O'):
                count += 1
                column += 1

    if count == 4:
        state = True

    return state

column = 0
while column != -1:
    column = column_choosing(grids, 1)
    system('cls')
    if (column == -1):
        break
    if (check_horizontal_win(grids, column) or check_vertical_win(grids, column) or check_top_left_win(grids, column) or check_top_rigth_win(grids, column)):
        print_grid(grids)
        print(f"Le joueur 1 ayant le caractère O a gagné")
        break
    column = column_choosing(grids, 2)
    system('cls')
    if (column == -1):
        break
    if (check_horizontal_win(grids, column) or check_vertical_win(grids, column) or check_top_left_win(grids, column) or check_top_rigth_win(grids, column)):
        print_grid(grids)
        print(f"Le joueur 2 ayant le caractère X a gagné")
        break

# print_grid(grids)
# print(check_top_left_win(grids, 3))


