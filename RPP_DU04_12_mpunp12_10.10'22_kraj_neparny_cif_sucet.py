import random
b,c = [],[]
d = 0
pocet = int(input(f'zadaj pocet cisel: '))
for i in range(pocet):
    a = random.randrange(99,1000)
    b.append(a)             # nahodne cislo
    a = str(a)
    for i in range(3):      # cif sucet nahodneho cisla
        d += int(a[i])
    c.append(d)
    d = 0

for i in range(pocet):
    if c[i]%2 == 0:
        print(f'cislo{i}: {b[i]}     cif.sucet: {c[i]}    je parne')
    else:
        print(f'cislo{i}: {b[i]}     cif.sucet: {c[i]}    nie je parne')
