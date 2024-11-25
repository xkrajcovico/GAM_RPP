import random
prve,druh = [],[]
with open ("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/textaky/list_txt_16.11'22_kraj_RPP_pole.txt",'a',encoding = 'utf-8') as subor:
    pocet = int(input(f'sem zadaj pocet prvkov dvoch poli: '))
    for i in range(pocet):
        prve.append(random.randrange(10,100))
    for i in range(pocet):
        druh.append(random.randrange(10,100))
    print(prve, druh)
    spolu = prve + druh
    print(f'najvacsi prvok: {max(spolu)}, najmensi prvok: {min(spolu)}', file = subor)