def mincovka():
    vstup = int(input(f'sem daj vstup'))
    petsto,sto,padesiat,dvadsat,desat,pet,dva,jeden = 0,0,0,0,0,0,0,0
    while vstup != 0:
        while vstup >= 500:                              # 500 - petsto
            vstup = vstup - 500
            petsto +=1
        while vstup >= 100:                              # 100 - sto
            vstup = vstup - 100
            sto +=1
        while vstup >= 50:                              # 50 - padesiat
            vstup = vstup - 50
            padesiat +=1
        while vstup >= 20:                              # 20 - davdsat
            vstup = vstup - 20
            dvadsat +=1
        while vstup >= 10:                              # 10 - desat
            vstup = vstup - 10
            desat +=1
        while vstup >= 5:                              # 5 - pet
            vstup = vstup - 5
            pet +=1
        while vstup >= 2:                              # 2 - dva
            vstup = vstup - 2
            dva +=1
        while vstup >= 1:                              # 1 - jeden
            vstup = vstup - 1
            jeden +=1
    print(f'500e . . . {petsto}ks\n100e . . . {sto}ks\n50e . . . {padesiat}ks\n20e . . . {dvadsat}ks\n10e . . . {desat}ks\n5e . . . {pet}ks\n2e . . . {dva}ks\n1e . . . {jeden}ks\n')
mincovka()