def longer_list(numbers: list[int]) -> list[int]:
    """
    Retourne la longueur de la plus longue sous-séquence
    croissante incluse dans une liste.

    Par exemple, la plus longue sous-séquence croissante de la liste :
    [16, 5, 10, 31, 2, 4, 19, 27, 3, 18] est [2, 4, 19, 27] et est donc de longueur 4

    """
    values = []
    for i in range(len(numbers) - 2):
        current_value = 1
        for j in range(i + 1, len(numbers) - 1):
            state = True
            while state:
                if numbers[i] < numbers[j]:
                    current_value += 1
                    i = j; j += 1
                else:
                    values.append(current_value)
                    state = False
                    break
            break

    return max(values)

# print(longer_list([16, 5, 10, 31, 2, 4, 19, 27, 3, 18]))