vstup = str(input(f'vstup: '))
out = 0
for znak in vstup:
    if znak.isdigit() == True:
        out += int(znak)
if out%2 == 0:
    print(f'pokračuj')
else:
    print(f'okamžite sa vráť domov')