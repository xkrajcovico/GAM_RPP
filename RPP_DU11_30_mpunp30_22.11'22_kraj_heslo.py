# # heslo nacitava
# heslo = str(input(f'zadaj heslo:'))

# # heslo si sam vytvori
# import random
# heslo = ''
# for i in range(random.randrange(50)):
#     string = chr(random.randrange(33,128))
#     heslo += string

velke_pismena = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'Z']
cisla = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(len(heslo)):
    if heslo[i] in velke_pismena:
        out1 = 1
    if heslo[i] in cisla:
        out2 = 1
with open("C:/Users/ondrej/Documents/school/IV.B GAM/RPP/Python/DU/txt/list_txt_22.11'22_kraj_RPP_heslo.txt",'w') as subor:
    if len(heslo) > 10 and out1 == 1 and out2 == 1:
        print(f'heslo({heslo}) je secure')
    else:
        print(f'heslo({heslo}) nie je secure')

