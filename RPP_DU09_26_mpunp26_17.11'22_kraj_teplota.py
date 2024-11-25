vstup = list(map(int,input(f'>>>:').strip().split()))
dni = ['pondelok', 'utorok', 'streda', 'stvrtok', 'piatok', 'sobota', 'nedela']
spolu,maxx = 0,0
with open ("C:/Users/ondrej/Documents/school/IV.B GAM/RPP/Python/DU/txt/list_txt_17.11'22_kraj_RPP_teploty.txt",'a',encoding = 'utf-8') as subor:
    for i in range(len(vstup)):
        if vstup[i] > maxx:
            maxx = vstup[i]
            den = i
        spolu += vstup[i]
    avrg = round(spolu/len(vstup), 2)
    print(f'Priemernáteplota bola: {avrg} °C', file = subor)
    print(f'Najteplejšie bolo {dni[den]}, bolo v: {maxx} °C',file = subor)
    
    for i in range(len(vstup)):
        print(f'V dni {dni[i]} bolo namerané: {vstup[i]}°C',file = subor)