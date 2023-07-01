def longer_list(numbers: list[int]) -> list[int]:
    """
    Retourne la longueur de la plus longue sous-séquence
    croissante incluse dans une liste.

    Par exemple, la plus longue sous-séquence croissante de la liste :
    [16, 5, 10, 31, 2, 4, 19, 27, 3, 18] est [2, 4, 19, 27] et est donc de longueur 4

    """
    values = []
    n = 0; k = len(numbers) - 1

    for i in range(n, k):
        current_value  = 1
        if numbers[i] < numbers[i + 1]:
            state = True
            while state and i <= len(numbers) - 2:
                if numbers[i] < numbers[i + 1]:
                    current_value += 1
                    i += 1
                else:
                    state = False
            else:
                values.append(current_value)
                state = False
                
    print(values)
    return max(values)

print(longer_list([16, 5, 10, 31, 2, 4, 19, 27, 3, 18]))