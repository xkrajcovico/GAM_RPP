vstup = input().strip().split() #  [100, 200, 150, 300, 250, 190] 
i,out = 0,0
while i+1 != len(vstup):
    if vstup[i] < vstup[i+1]:
        print(f'úsek {i}: {vstup[i]} - {vstup[i+1]} - stúpanie')
        out += 1
    else:
        print(f'úsek {i}: {vstup[i]} - {vstup[i+1]} - klesanie')
        out += -1
    i += 1
if out > 0:
    print('Viac úsekov bolo stúpajúcich.')
else:
    print('Viac úsekov bolo klesajúcich.')