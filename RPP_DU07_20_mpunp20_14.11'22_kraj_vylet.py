with open("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/textaky/list_txt_14.11'22_kraj_RPP_vylet.txt", "r", encoding = 'utf-8') as subor:
    cena = int(input(f'Zadaj cenu cestovného pre 1 osobu: '))
    out,mlad = 0,0
    text = subor.readlines()
    for i in range(len(text)):
        if i%2 != 0:
            if int(text[i]) <= 15:
                mlad += 1
                out += cena/2
            else:
                out += cena
    print(f'cena za osobu: {cena}')
    print(f'cena spolu: {out}')
    print(f'pocet osob: {len(text)//2}')
    print(f'z toho mladsich ako 15: {mlad}')
# list_txt_14.11'22_kraj_RPP_vylet.txt
# jana cmurka
# 11
# janko hrasko
# 25
# simka cinka
# 55
# anna julkova
# 19
# raxakorykofalapatorius o
# 15555