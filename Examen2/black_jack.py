from random import randint

def random_card() ->  list[str]:
    """
    Fonction qui retourne une carte (liste de taille 2)
    dont la valeur faciale et la couleur sont aléatoires
    """
    possibilities = [
        ['2', 'coeur'], ['3', 'coeur'], ['4', 'coeur'], ['5', 'coeur'], ['6', 'coeur'], ['7', 'coeur'], ['8', 'coeur'], ['9', 'coeur'], ['10', 'coeur'],
        ['valet', 'coeur'], ['dame', 'coeur'], ['roi', 'coeur'], ['as', 'coeur'],

        ['2', 'pique'], ['3', 'pique'], ['4', 'pique'], ['5', 'pique'], ['6', 'pique'], ['7', 'pique'], ['8', 'pique'], ['9', 'pique'], ['10', 'pique'],
        ['valet', 'pique'], ['dame', 'pique'], ['roi', 'pique'], ['as', 'pique'],

        ['2', 'trèfle'], ['3', 'trèfle'], ['4', 'trèfle'], ['5', 'trèfle'], ['6', 'trèfle'], ['7', 'trèfle'], ['8', 'trèfle'], ['9', 'trèfle'], ['10', 'trèfle'],
        ['valet', 'trèfle'], ['dame', 'trèfle'], ['roi', 'trèfle'], ['as', 'trèfle'],

        ['2', 'carreau'], ['3', 'carreau'], ['4', 'carreau'], ['5', 'carreau'], ['6', 'carreau'], ['7', 'carreau'], ['8', 'carreau'], ['9', 'carreau'], ['10', 'carreau'],
        ['valet', 'carreau'], ['dame', 'carreau'], ['roi', 'carreau'], ['as', 'carreau'],
    ]

    random_number = randint(0, len(possibilities) - 1)

    return possibilities[random_number]

# card = random_card()

# print(card)

def total_cards(items: list[list[str]]) -> int:
    """
    Fonction qui retourne le nombre de points correspondant à une main
    """
    total = 0
    for item in items:
        if item[0] == 'as':
            if (total + 11) <= 21:
                total += 11
            else:
                total += 1
        elif item[0] in ('valet', 'dame', 'roi'):
            total += 10
        else:
            total += int(item[0])

    return total

# total = total_cards([['5', 'carreau'], ['5', 'coeur'], ['as', 'trèfle']])
# print(total)

def card_game():
    """
    Fonction simulant le jeu Blackjack
    """
    player_cards = []
    total = 0
    res = 'y'.upper
    while (res == 'yes'.upper or res == 'y'.upper) and total <= 21:
        res = input("Voulez-vous tirer une carte (y/n) : ").upper
        if res == 'y'.upper or res == 'yes'.upper:
            player_cards.append(random_card())
            total = total_cards(player_cards)
            if total > 21:
                break
            else:
                print(f"Main : {player_cards}")
                print(f"Nombre de points : {total}")
    if total > 21:
        total = 0
        print(f"Nombre total de points : {total}")
    else:
        print(f"Nombre total de points : {total}")


card_game()
