import random
i = 0
cislo = random.randrange(100)
with open ("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/textaky/list_txt_16.11'22_kraj_RPP_hadaj.txt",'a',encoding = 'utf-8') as subor:
    tvoje = int(input(f'Zadaj tvoj tip (od 1 do 100):'))
    while tvoje != cislo:
        if tvoje < cislo:
            print(f'Tip bol menší ako číslo. Skús hádať ďalej! ')
        else:
            print(f'Tip bol väčší ako číslo. Skús hádať ďalej! ')
        tvoje = int(input(f'Zadaj tvoj tip (od 1 do 100):'))
        i += 1
    meno = str(input(f'Zadaj svoje meno: '))
    print(f'{meno}, uhádol/la si na {i}. pokus', file = subor)
    print(f'{meno}, uhádol/la si na {i}. pokus')