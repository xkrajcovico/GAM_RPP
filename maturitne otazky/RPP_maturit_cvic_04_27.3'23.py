import random

n = int(input())
out = [0]             #[pocet, index]

intigers = []
for i in range(n):
    intigers.append(random.randrange(100,1000))

# intigers = [634,718,981]

def cs(cislo):
    cislo = str(cislo)
    sucet = 0
    for char in  str(cislo):
        sucet += int(char)
    return sucet

for i in range(n):
    if cs(intigers[i]) % 2 != 0:
        out[0] += 1
        out.append(i)
        
print(f'pocet: {out[0]}')
for i in range(out[0]):
    print(intigers[out[i-1]])