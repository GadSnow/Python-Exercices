def lowest_number():
    n = 0
    for i in range (8,2023):
        n += i
        if n > 2023:
            n = i 
            break;
    print (f"La plus petite valeur de n est {n}");

lowest_number()