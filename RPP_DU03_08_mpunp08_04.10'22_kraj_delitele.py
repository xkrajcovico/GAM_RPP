def vypis_delitele(cislo,hranica):
    with open("C:/Users/ondrej/Documents/school/IV.B GAM/RPP/Python/DU/txt/delitele_kraj.txt","w") as subor:
        for i in range(hranica):
            if cislo % (i+1) == 0:
                print(f'{i+1}', file = subor)