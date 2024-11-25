text = []
suc = []
i = 0
null = -1023
with open("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/textaky/meteo_stanice.txt",'r') as subor:
    for line in subor:
        text.append(line.strip().split(' '))
        prvok = float(text[i][3].replace(',','.'))
        suc.append(prvok)
        i +=1
        if prvok > int(max(suc)):
            maxi = text[i-1][0]
    print(f'pocet merani: {len(text)}')
    print(f'Maximum bolo v stanici: {maxi}')
    print(f'average: {round(sum(suc)/len(text),2)}')
