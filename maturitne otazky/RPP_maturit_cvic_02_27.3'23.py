samohlasky = 'aeiouy'
out = [0,0,0]
with open('C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/maturitne_cvivenie/txt/telegram.txt', 'r', encoding= 'UTF-8') as file:
    text = file.read()
    for char in text:
        if char == ' ':
            out[0] += 1
        elif char in samohlasky:
            out[1] +=1
        elif char.isupper() == True:
            out[2] +=1
print(f'Pocet samohlasok: {out[1]}\nPocet velkych pismen: {out[2]}\npocet medzier: {out[0]}')