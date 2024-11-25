n = int(input(f'->'))
m = []
riadok = []
for i in range(1,2+n*n):
    if len(riadok) != n:
        riadok.append(i)
    else:
        m.append(riadok)
        riadok = [i]
print(m)