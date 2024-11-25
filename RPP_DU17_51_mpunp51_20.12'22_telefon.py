vstup = input().strip().split(' ')
vstup = list(map(int,vstup))
vstup = sum(vstup)
cas = []
while vstup != 0:
    cas.append(vstup % 60)
    vstup = vstup // 60
cas.append(0)    
print(cas)
print(f'{cas[-1]} hod. {cas[-2]} min. {cas[-3]} sek.')