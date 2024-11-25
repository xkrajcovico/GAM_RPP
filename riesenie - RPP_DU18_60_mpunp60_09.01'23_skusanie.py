import random
studenti = int(input('počet študentov: '))
otazky = int(input('počet otázok: '))
if studenti > otazky:
    print('študentov je viac ako otázok')
else:
    pole_st = []
    pole_ot_p = []
    pole_ot_n = []
    for i in range(1,studenti+1):
        pole_st.append(i)
    random.shuffle(pole_st)
    print(pole_st)

    for i in range(1,otazky+1):
        if i % 2==0:
            pole_ot_p.append(i)
        else:
            pole_ot_n.append(i)
    random.shuffle(pole_ot_p)
    print(pole_ot_p)
    random.shuffle(pole_ot_n)
    print(pole_ot_n)
    pole_ot = []
    for i in range(otazky//2):
        pole_ot.append(pole_ot_p[i])
        pole_ot.append(pole_ot_n[i])
    for i in range(0,studenti):
        print(f'{i+1}.študent má poradové číslo: {pole_st[i]}, otázku číslo {pole_ot[i]}')



### bez zadania počtu študentov a otázok
import random
studenti = 30
otazky = 50
pole_st = []
pole_ot_p = []
pole_ot_n = []

for i in range(1,studenti+1):
    pole_st.append(i)
random.shuffle(pole_st)
print(pole_st)

for i in range(1,otazky+1):
    if i % 2==0:
        pole_ot_p.append(i)
    else:
        pole_ot_n.append(i)
random.shuffle(pole_ot_p)
print(pole_ot_p)
random.shuffle(pole_ot_n)
print(pole_ot_n)

pole_ot = []
for i in range(otazky//2):
    pole_ot.append(pole_ot_p[i])
    pole_ot.append(pole_ot_n[i])
for i in range(0,studenti):
    print(f'{i+1}.študent má poradové číslo: {pole_st[i]}, otázku číslo {pole_ot[i]}')
