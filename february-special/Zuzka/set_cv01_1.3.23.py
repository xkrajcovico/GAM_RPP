from random import randrange
number = ''
for i in range(8):
    number += str(randrange(10))

uz_bolo,s = set(),set()

for char in number:
    if char in s or char in uz_bolo:
        uz_bolo.add(char)
    else:
        s.add(char)
s = s - uz_bolo

if len(s) == 0:
    print(f'neda sa')
else:
    list = sorted(s, reverse= True)
    for char in list:
        print(char, end= '')