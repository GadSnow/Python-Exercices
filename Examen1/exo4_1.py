from random import randint

def random_number(a, b) -> int:
    return randint(a, b)

random_value = random_number(1, 2)

# print(f"Le nombre aléatoire généré est {random_value}")