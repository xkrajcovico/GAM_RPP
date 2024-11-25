with open("C:/Users/ondrej/Documents/school/IV.B GAM/RPP/Python/DU/txt/kvadraticka_kraj.txt","w") as subor:
    x = -20
    for i in range(21):
        print(f'x = {x}          y = {x**2+3*x-2}', file = subor)
        x += 2