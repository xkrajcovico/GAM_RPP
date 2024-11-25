import random
with open("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/textaky/poprehadzovany_text1_vstup.txt", 'r', encoding = 'UTF-8') as subor:
    text = subor.read().strip().split()
    zaciatok, konec = [],[]
    for slovo in text:
        pismenka = list(slovo)
        zaciatok = pismenka[0]
        konec = pismenka[-1]
        slovo = slovo[1:-1]
        pismenka = list(slovo)
        random.shuffle(pismenka)
        slovo = ''
        for j in range(len(pismenka)):
            slovo = slovo + pismenka[j]
        slovo = zaciatok + slovo + konec
        print(slovo, end = ' ')
