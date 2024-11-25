i = 0
zz = []
cislo = int(input(f'zadaj znamku'))
while cislo != -1:
    cislo = int(input(f'zadaj znamku'))
    if cislo != -1:
        zz.append(cislo)
    i += 1
print(f'znamky boly: {zz}\nnajmenej bodov: {min(zz)}\nnajviac bodov: {max(zz)}\npriemer: {(sum(zz)/len(zz))}')
