with open ('C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/maturitne_cvivenie/txt/telegram.txt', 'r', encoding= 'UTF-8') as file:
    text = file.read()
    out = ''
    for char in text:
        if char.isdigit() == True or char.isupper() == True:
            out += '_'
        else:
            out += char

with open ('C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/maturitne_cvivenie/txt/vystup.txt', 'w', encoding= 'UTF-8') as file:
    print(out, file= file)