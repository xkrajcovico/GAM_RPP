vstup = str(input(f'>>>'))
pole = vstup.strip().split()
print(f'pocet slov: {len(pole)}')
for i in range(len(pole)):
    if i%2 == 0:
        pole[i] = pole[i].upper()
    print(pole[i], end = '')
print('')
for i in range(len(pole)):
    print(f'{pole[i].upper()} ', end = '')