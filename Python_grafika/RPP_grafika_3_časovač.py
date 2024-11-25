'''
For cyklus používame v situáciách, keď vopred vieme odhadnúť počet opakovaní
cyklu. Aj preto sa mu zvykne hovoriť cyklus s pevným počtom opakovaní.
Sú však situácie, keď potrebujeme opakovať nejakú činnosť v pravidelných časových
intervaloch a vopred nepoznáme presný počet opakovaní. Na riešenie takéhoto
problému môžeme použiť takzvaný časovač (timer), ktorý v pravidelných časových
intervaloch opakuje zadanú postupnosť príkazov.
Na to sa využíva príkaz
canvas.after(čas, funkcia),
ktorému zadávame okrem
času v milisekundách aj meno funkcie, ktorá sa má vykonať po pozdržaní programu.

'''

import tkinter, random
canvas = tkinter.Canvas()
canvas.pack()
def kruzok():
    x = random.randrange(450)
    y = random.randrange(320)
    if 100<x<150 or 50<y<100:
        canvas.create_oval(x-5, y-5, x+5, y+5, fill='green')
    else:
        canvas.create_oval(x-5, y-5, x+5, y+5, fill='yellow')
    canvas.after(10, kruzok)
    
def stvorec():
    x = random.randrange(450)  
    y = random.randrange(320)
    if 100<x<150 or 50<y<100:
        canvas.create_rectangle(x-5, y-5, x+5, y+5, fill='red')
    else:
        canvas.create_rectangle(x-5, y-5, x+5, y+5, fill = 'blue')
    canvas.after(30, stvorec)

kruzok()
#stvorec()
'''
V programe sme nastavili premennú x na hodnotu 200 a y na hodnotu 5.
V týchto premenných si pamätáme súradnice, kde sa nakreslí prvá loptička.
Po nastavení premenných spustíme funkciu lopticka.
Táto funkcia nakreslí loptičku (krúžok) na súradniciach podľa hodnôt
premenných x a y. Ďalšiu loptičku chceme nakresliť o 5 bodov nižšie.
Preto zvýšime y o 5, čiže zapíšeme y = y+5. Keďže sme vo funkcii lopticka,
nemôžeme tu bežne meniť hodnotu premennej, ktorá sa používa
v hlavnom programe mimo našej funkcie.
Premenné y aj x sú globálne premenné, a nie lokálne premenné vo funkcii,
kde ich chceme meniť. V takejto
situácii musíme použiť príkaz global a meno premennej,
aby sme funkcii oznámili, že chceme pracovať s globálnou premennou.
Teraz má y hodnotu 10.
V ďalšom riadku sa pýtame, či y je menšie ako 200, a iba ak je
táto podmienka splnená,
naplánujeme ďalšie spustenie funkcie lopticka o 100 milisekúnd.
Vidíme, že sme vytvorili časovač, ktorý neopakuje príkazy donekonečna,
ale len kým je splnená podmienka. Po
spustení programu budeme vidieť, ako sa kreslí viacero loptičiek pod sebou.
'''
##import tkinter
##canvas = tkinter.Canvas()
##canvas.pack()
##
##def lopticka():
##    #canvas.delete('all')
##    global y
##    canvas.create_oval(x-5, y-5, x+5, y+5)
##    y = y+10
##    if y<200:
##        canvas.after(100, lopticka)
##x = 200
##y = 5
##lopticka()



