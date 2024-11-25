vstup = str(input(f'   >>>'))
dlzka = int(input(f'   >>>'))
out = 0
i = 0
while i+2 != len(vstup):
    if vstup[i] == vstup[i+dlzka-1]:
        out += 1
    i += 1
print(out) 