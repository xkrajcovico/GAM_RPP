import datetime
with open("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/textaky/sutaz_vbehu.txt",'r', encoding= 'utf-8') as subor:
    text = []
    max = 10000000
    for line in subor:
        text.append(line.strip().split())
    for i in range(len(text)):
        print(f'Súťažiaci {text[i][0]} dobehol za {text[i][1]} sekúnd')
        if int(text[i][1]) < max:
            max = int(text[i][1])
            sutaziaci = text[i][0]
    minuty = max//60
    sekundy = max - minuty*60
    print(f'Počet zúčastnených športovcov: {i+1}')
    # print(f'Najlepší športovec: {sutaziaci} s časom {datetime.timedelta(seconds=max)}')
    print(f'Najlepší športovec: {sutaziaci} s časom {minuty} min. a {sekundy} sek.')
