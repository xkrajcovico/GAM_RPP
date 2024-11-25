with open("C:/Users/ondrej/Documents/school/IV.B GAM/RPP/Python/DU/txt/rodne_cisla.txt",'r',encoding = 'UTF-8') as subor:
    for riadok in subor:
        if int(riadok[5]) == 5 or int(riadok[5]) == 6:
            print(f'{riadok[0:2]}, nar. {riadok[7:9]}.0{int(riadok[5:7])-50}.{riadok[3:5]}, žena')
        else:
            print(f'{riadok[0:2]}, nar. {riadok[7:9]}.{riadok[5:7]}.{riadok[3:5]}, muž')