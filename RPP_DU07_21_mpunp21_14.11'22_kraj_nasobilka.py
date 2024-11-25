import random
with open("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/textaky/list_txt_14.11'22_kraj_RPP_nasobilka.txt", "a", encoding = 'utf-8') as subor:
    out = 0
    for i in range(10):
        cislo1 = random.randrange(10)
        cislo2 = random.randrange(10)
        vstup = int(input(f'{cislo1} * {cislo2} = '))
        if vstup == cislo1 * cislo2:
            out += 1
            print('spravne')
            print(f'{cislo1} * {cislo2} = {vstup}', file = subor)
        else:
            print('nespravne')
    print(out)