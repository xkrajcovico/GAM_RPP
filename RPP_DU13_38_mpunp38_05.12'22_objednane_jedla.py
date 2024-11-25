z,c,o,m,i = 0,0,0,0,0
text  = []
with open("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/textaky/objednane_jedla.txt","r") as subor:
    for line in subor:
        text.append(line.strip().split(' '))
        if str(text[i][1]) == 'z':
            z += 1
        elif str(text[i][1]) == 'c':
            c += 1
        elif str(text[i][1]) == 'o':
            o += 1 
        else:
            m += 1
        i += 1
    print(f'počet jedál: {z + c + m + o}')
    print(f'Kod jedla: z počet objednávok:{z}')
    print(f'Kod jedla: c počet objednávok:{c}')
    print(f'Kod jedla: o počet objednávok:{o}')
    print(f'Kod jedla: m počet objednávok:{m}')
    # [insert minimum of function]
    x = [z ,  c ,  m ,  o].index(min([z ,  c ,  m ,  o]))
    if x == 0:
        print('z')
    elif x == 1:
        print('c')
    elif x == 2:
        print('m')
    else:
        print('o')
    # print(text)