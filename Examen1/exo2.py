def twelve_calculus():
    for i in range(20, 255):
        s = 0
        temp = i
        while i != 0:
            s += int(i % 10)
            i = int(i / 10)
        if s == 12:
            print(temp)

twelve_calculus()
