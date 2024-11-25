import random
pocet_student = int(input(f'Zadaj počet študentov: '))
pocet_otazok = int(input(f'Zadaj počet otázok: '))
zalezi = input(f'chces aby sa parne a neparne otazky striedali? ')
print('Poradie odpovedajúcich a ich číslo otázky:')
otazky_parne, otazky_neparne = [],[]
for i in range(1,pocet_otazok+1):
    if i%2 == 0:
        otazky_parne.append(i)
    else:
        otazky_neparne.append(i)
 
uzbol_student = []
uzbol_otazka = []

if zalezi == 'áno' or zalezi == 'ano' or zalezi == 1:
    for i in range(pocet_student):

        student = random.randrange(pocet_student)
        while student in uzbol_student:
            student = random.randrange(pocet_student)
        uzbol_student.append(student)

        if i%2 == 0:
            otazka = int(random.choice(otazky_parne))
            while otazka in uzbol_otazka:
                otazka = int(random.choice(otazky_parne))
            uzbol_otazka.append(otazka)
            print(f'{i+1}. študent: {student+1}, otazka: {otazka}')

        elif i%2 != 0:
            otazka = int(random.choice(otazky_neparne))
            while otazka in uzbol_otazka:
                otazka = int(random.choice(otazky_neparne))
            uzbol_otazka.append(otazka)
            print(f'{i+1}. študent: {student+1}, otazka: {otazka}')

else:
    for i in range(pocet_student):

        student = random.randrange(pocet_student)
        while student in uzbol_student:
            student = random.randrange(pocet_student)
        uzbol_student.append(student)

        otazka = random.randrange(pocet_otazok)
        while otazka in uzbol_otazka:
            otazka = random.randrange(pocet_otazok)
        uzbol_otazka.append(otazka)
        print(f'{i+1}. študent: {student+1}, otazka: {otazka}')