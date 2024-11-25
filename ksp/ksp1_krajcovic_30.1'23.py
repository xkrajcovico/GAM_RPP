from random import randrange
f = 100
n,v,k = randrange(f),randrange(f),randrange(f)
n,v,k = int(n),int(v), int(k)
m = f//2
skaly = []
# n - pocet skal
# v - pocet veducich
# k - vyska skoku veduceho
# input().strip().split()
for i in range(n):
    skaly.append(randrange(m)+1)
print(f'-----------------\nn = {n},v = {v},k = {k},\nm = {m},\nskaly ={skaly}')
print()
# skaly = input().strip().split()
skaly = list(map(int,skaly))
for i in range(len(skaly)):
    if k >= skaly[i]:
        continue
    else:
        v = v - skaly[i]
        if v <= 0:
            print(f'nepresli sme cez skalu cislo {skaly[i-1]}')
            break
        else:
            continue
if v > 0:
    print(f'na chatu dorazilo {v} veducich')
