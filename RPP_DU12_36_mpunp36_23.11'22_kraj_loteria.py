import random
zreb,out = [],[]
while len(zreb) != 6:
    prvok = random.randrange(1,50)
    if prvok not in zreb:
        zreb.append(prvok)

guess = input(f'Zadaj svoje čísla: ').strip().split()
guess = list(map(int,guess))
zreb = list(map(int,zreb))

for prvok in zreb:
    if prvok in guess:
        out.append(prvok)
print(f'Vyžrebované čísla:  {zreb}')
print(f'Počet uhádnutých čísel: {len(out)}, je to:  {out}')