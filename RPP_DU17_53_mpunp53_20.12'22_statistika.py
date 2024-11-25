import random
def generuj_body():
    out = []
    for i in range(100):
        out.append(int(random.randrange(6)+1))
    return out
def padla_trojica(trojica,pole):
    tri = []
    for i in range(3):
        tri.append(str(trojica)[i])
    out1,out2,i = 0,0,0
    while i + 2 != len(pole):
        if pole[i] == tri[1] and pole[i + 1] == tri[2] and pole[i +2] == tri[2]:
            out1 += 1
        elif pole[i] == tri[2] and pole[i - 1] == tri[1] and pole[i +2] == tri[0]:
            out2 += 1
        i += 1
    print(f'{out1}. Čísla nepadli za sebou v rovnakom poradí.')
    print(f'{out2}. Čísla padli za sebou v opačnom poradí.')
# pole = generuj_body()
# padla_trojica(456,pole)
# print(pole)