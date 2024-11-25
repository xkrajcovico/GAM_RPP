###cv_05_mpunp_kraj_03.10'22_bmi
##vyska = int(input(f'vyska(m): '))
##vaha = int(input(f'vaha(kg): '))
obezny =0
def bmi(vyska,vaha):
    with open("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/python/Maturitne otazky/textaky/list_txt_03.10'22_kraj_RPP_BMI.txt","a",encoding = 'utf-8') as subor:
        bmi = vaha/(vyska**2)
        print(round(bmi,2))
        print(f'tvoje bmi je {round(bmi,2)}',file = subor)
        if bmi >= 30:
            return True
        else:
            return False


#with open ("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/python/Maturitne otazky/textaky/list_txt_03.10'22_kraj_RPP_BMI.txt","a",encoding = 'utf-8') as subor:
n = int(input(f'sem zadaj pocet ziakov: '))
for i in range(n):
    bmi(float(input(f'vyska: ')), int(input(f'vaha: ')))
    if bmi:
        obezny += 1
print(f'obeznych je {(obezny/(n))*100}% ziakov')



##bmi(int(input(f'vyska: ')), int(input(f'vaha: ')))
