def sifruj_s_posunom(text, posun):
    out = ''
    for znak in text:
        posunutie = ord(znak) + posun
        out += chr(posunutie)
    print(out)
def desifruj_s_posunom(text, posun):
    out = ''
    for znak in text:
        posunutie = ord(znak) - posun
        out += chr(posunutie)
    print(out)
with open ("C:/Users/ondrej/Documents/school/IV.B GAM/RPP/Python/DU/txt/list_txt_17.11'22_kraj_RPP_cezarova_sifra.txt",'w',encoding = 'utf-8') as subor:
    for i in range(24):
        print(desifruj_s_posunom('gqhv#pdwxuxmhp', i), file = subor)