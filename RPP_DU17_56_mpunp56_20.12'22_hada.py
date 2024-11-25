with open("C:/Users/ondrej/Documents/school/IV.B GAM/RPP/Python/DU/txt/hada.txt",'r', encoding='UTF-8') as subor:

    pocet,i,j,lenght = 0,0,0,[]
    for riadok in subor:

        riadok = riadok + 'i'
        j = 0
        for i in range(len(riadok)):
            if riadok[i] != 'i':
                j += 1
                if riadok[i] != riadok [i+1]:
                    print(riadok[i],j,' ', end = '')

                    j = 0
        print('')
        pocet += 1
        lenght.append(len(riadok))
    print(f'Počet riadkov v súbore: {pocet}')
    print(f'Počet krokov v najdlhšej hre: {max(lenght)}')