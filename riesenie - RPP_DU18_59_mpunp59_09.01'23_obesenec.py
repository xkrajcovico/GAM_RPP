import random
with open('obesenec.txt', 'r', encoding = 'utf-8') as subor:
    slova = subor.readlines()
print(slova)
#odstránim

cislo = random.randrange(len(slova))
hadane = slova[cislo]
hadane = hadane.strip() #odstránim koncový enter \n
print(hadane)
#print(len(hadane))

print('Hádaj písmená v slove.')
nove = '.'*len(hadane)
print(nove)
c = 1
while hadane != nove:
    pism = input('zadaj písmenko: ')
    if pism in hadane:
        index = hadane.index(pism)
        print(index)
        if index ==0:
            nove = pism +nove[1:]
            print(nove)
        elif index == len(hadane)-1:
            nove = nove[:index] + pism
            print(nove)
        else:
            nove = nove[:index] + pism +nove[index+1:]
            print(nove)
    c +=1
    if c > 10:
        print('neuspel si')
        break
    if hadane == nove:
        print('Blahoželám, uhádol si')
        break
