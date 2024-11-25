###RPP_12.9'22_kraj_cv01_dec->bin
##cislo = int(input(f'sem zadaj cislo na preradenie'))
##out,sucet = '',''
##
##while cislo != 0:
##    sucet += str(cislo % 2)
##    cislo = cislo //2
##   
##for i in range(len(sucet)):
##    out += sucet[-(i+1)]
##
##print(f'tvoje cislo v bin sustave je: {out}')

###RPP_12.9'22_kraj_cv02_biin -> dec
##cislo = str(input(f'sem zadaj cislo na preradenie'))
##pole = list(cislo)
##pole = list(map(int,pole))
##pole.reverse()
##out = 0
##for i,prvok in enumerate(pole):
##    out = out + prvok * 2**i
##print(f'tvoje cislo v decadickej sustave je: {out}')

###RPP_12.9'22_kraj_cv02_dec->hex
##cislo = int(input(f'sem zadaj cislo na preradenie'))
##out,sucet = '',''
##
##while cislo != 0:
##    if cislo%16 >= 10:
##        if cislo % 16 == 10:
##            sucet = 'A'
##        elif cislo%16 == 11:
##            sucet = 'B'
##        elif cislo%16 == 12:
##            sucet = 'c'
##        elif cislo%16 == 13:
##            sucet = 'D'
##        elif cislo%16 == 14:
##            sucet = 'E'
##        elif cislo%16 == 15:
##            sucet = 'F'
##    else: sucet = str(cislo%16)
##    out = sucet + out
##    cislo = cislo //16
##print(out)
