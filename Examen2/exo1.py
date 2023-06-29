from random import randint

def random_number(n: int) -> list[int]:
    """Programme générant des nombres aléatoires de 1 à n

    Par exemple, si n = 10 une permutation aléatoire de l’ensemble des
    entiers de 1 à 10 peut être la suivante : [6, 5, 10, 1, 2, 4, 9, 7, 3, 8].
    """
    numbers = []
    while len(numbers) != 10:
        value = randint(1, n)
        if value in numbers:
            pass
        else:
            numbers.append(value)
    return numbers

# print(random_number(10))