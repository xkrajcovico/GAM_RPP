import random
with open("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/textaky/obesenec.txt", 'r', encoding='UTF-8') as subor:
    text = subor.read()
# print(text)

slovo = random.choice(text.split())
guess = len(slovo)*['.']
a = 0
while guess != slovo:
    out = ''
    for i in range(len(slovo)):
        out = out + guess[i]
    print(out)
    if out == slovo:
        print('Gratulujem, uhádol si celé slovo!')
        break
    if a >= 10:
        print('prehral si')
        break
    pokus = str(input(f'Zadaj jedno pismeno: '))
    if pokus in list(slovo):
        pozicia  = list(slovo).index(pokus)
        # print(pozicia)
        guess[pozicia] = pokus
    a += 1