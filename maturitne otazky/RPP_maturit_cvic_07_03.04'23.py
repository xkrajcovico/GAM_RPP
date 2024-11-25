t = int(input())

for i in range(t):
    c1 = int(input()) #velka
    v1 = int(input())
    c2 = int(input()) #mala
    v2 = int(input())
    if c1 / v1 <= c2/v2:
        print('Vacsie')
    else:
        print('Mensie')