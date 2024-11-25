text = []
with open("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/textaky/dopravny_prieskum.txt","r") as subor:
    for line in subor:
        text.append(line.strip().split(';'))
    j = 0
    spolu = 0
    auto = []
    sedi = []
    znam = []
    cely = subor.read().strip()
    for i in range(len(text)):
        # print(f'na zastávke {text[i][j+2]} nastúpilo: {text[i][j]} ludí a vystúpilo: {text[i][j+1]} ludí')
        spolu += int(text[i][j]) - int(text[i][j+1])
        sedi.append(spolu)
        # print(f' po zastavke {text[i][j+2]} sedí v MHD {spolu} ludi', end = '')
        if int(text[i][j]) > 10:
            # print(f' - na túto zastávku sa oplatí nainštalovať automat')
            auto.append(text[i])
        elif i != len(text)-1 and int(text[i][j]) < 3 and int(text[i][j+1]) < 3:
            # print(' - túto zastávku sa oplati rekvalifikovat ako na znamenie')
            znam.append(text[i])
        else:
            print('')
        j +1
    # zoznam 01 - Zastávka -Počet cestujúcich. 
    print(f'\nZastávka -Počet cestujúcich')
    for i in range(len(sedi)):
        print(f'Po zastavke {text[i][2]} sedí {sedi[i]}')
    # zoznam 02 - sem by sa oplatil automat:
    print(f'\nZastávky vhodné na umiestnenie automatu')
    for i in range(len(auto)):
        print(f'{auto[i][2]}')
    # zoznam 03 zastavkana znamenie
    print(f'\nVhodné zastávky na znamenie:')
    for i in range(len(znam)):
        print(f'{znam[i][2]}')
# for j in range(len(text)):
