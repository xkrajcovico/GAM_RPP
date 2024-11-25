with open ("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/textaky/list_txt_16.11'22_kraj_RPP_sms.txt",'r',encoding = 'utf-8') as subor:
    hlas = []
    out = 10000000000
    for riadok in subor:
        riadok = riadok.strip().split()
        hlas = list(map(int,hlas))
        hlas.append(riadok[1])
    for i in range(len(hlas)):
        if out >= int(hlas[i]):
            out = int(hlas[i])
    print(f'Najmenej hlasov: {out}, mal súťažiaci s číslom 693{hlas.index(out)}')
        
    