def pyramid_number():
    n = int(input("Entrez un entier : "))
    print("Voici la pyramide de nombres")
    for i in range (1, (n + 1)):
        print(f"{i} : ", end="")
        for j in range (1, (i + 1)):
            print(pow(j, 2), end=" ")
        print()


pyramid_number()