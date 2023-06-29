from exo4_1 import random_number

a = b = c = 0

for i in range (3):
    if i == 0:
        a = random_number(1, 6)
    elif i == 1:
        b = random_number(1, 6)
    else:
        c = random_number(1, 6)

print(f"a = {a}, b = {b}, c = {c}")

a = 4; b = 1; c = 2

if (a == b == c):
    print("brelan")
elif (((b == a + 1) and (c == b + 1)) or ((b == a - 1) and (c == b - 1))):
    print("Suite")
elif (a == 1):
    if ((b == 2 and c == 4) or (b == 4 and c == 2)):
        print("421")
elif (a == 2):
    if ((b == 1 and c == 4) or (b == 4 and c == 1)):
        print("421")
elif (a == 4):
    if ((b == 2 and c == 1) or (b == 1 and c == 2)):
        print("421")
elif (a == b or b == c or a == c):
    print("Paire")
