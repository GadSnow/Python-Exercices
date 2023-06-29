from exo1 import random_number
from exo2 import longer_list

first_permutation = random_number(10)
second_permutation = random_number(10)

first_longer = longer_list(first_permutation)
second_longer = longer_list(second_permutation)

number_of_positions = 0

for i in range(len(first_permutation)):
    if first_permutation[i] == second_permutation[i]:
        number_of_positions += 1

print(f"Première permutation : {first_permutation}")
print(f"Seconde permutation : {second_permutation}")
print(f"Longueur de la plus longue  sous-sequence pour list 1: {first_longer}")
print(f"Longueur de la plus longue  sous-sequence pour list 2: {second_longer}")
print(f"Nombre de positions collisionnantes : {number_of_positions}")
