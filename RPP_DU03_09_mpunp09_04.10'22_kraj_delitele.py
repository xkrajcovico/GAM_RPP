with open("C:/Users/ondrej/Documents/school/IV.B GAM/RPP/Python/DU/txt/cif_sucet_kraj.txt","w") as subor:
    out = 0
    cislo = str(input(f'sem zadaj svoje cislo(od 10 do 20): '))
    print(f'v prvom stlpci je tvoje cislo v druhom ciferny sucet', file = subor)
    for sucet in cislo:
        out += int(sucet)
    print(f'{cislo}               {out}', file = subor)