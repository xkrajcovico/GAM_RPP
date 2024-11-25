with open("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/textaky/znamky.txt", 'r', encoding= 'utf-8') as subor:
    a = []
    b = []
    for i,line in enumerate(subor):
        if i%2 != 0:
            a.append(line.strip().split())
        else:
            b.append(line.strip())
    out = []
    for i in range(len(a)):
        spolu = 0
        for j in range(len(a[i])):
            if a[i][0].isdigit() == False:
                out.append(a[i][j])
            else:
                spolu += int(a[i][j])
        if a[i][j].isdigit() == True:
            out.append(round(spolu/len(a[i]),2))
    print(out, b)
        
    
with open("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/textaky/vysledky_znamky.txt", 'w') as subor:
    for i in range(len(out)):
        print(b[i], out[i], file = subor)