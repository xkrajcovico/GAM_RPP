###padajúca loptička
##import tkinter
##canvas = tkinter.Canvas()
##canvas.pack()
##
##def lopticka():
##    global y 
##    canvas.delete('all')
##    canvas.create_oval(x-5, y-5, x+5, y+5)
##    y = y+5
##    if y>250:
##        y = 5
##    if pokracovat == 1:
##        canvas.after(100, lopticka)
##def stop(suradnice):
##    global pokracovat
##    if pokracovat == 1:
##        pokracovat = 0
##    else:
##        pokracovat = 1
##        lopticka()
##pokracovat = 1
##x = 200
##y = 5
##lopticka()
##canvas.bind('<Button-1>',stop)

'''
Vytvorte program, ktorý bude postupne písať do canvasu 0 alebo 1 (náhodne si vyberá) a bude mať
tieto vlastnosti:
- program začína písať z ľavého horného rohu v jednom riadku, až kým ho nezaplní,
- keď sa zaplní jeden riadok, písanie pokračuje na ďalšom riadku (môžete si určiť, koľko ich má byť v
jednom riadku),
- 0 sa píše modrou farbou (resp. si vyberte farbu),
- 1 sa píše zelenou farbou (resp. si vyberte farbu),
- po stlačení klávesu p sa vypisovanie zastaví (pauza),
- opätovným stlačením klávesu p sa zapne pokračovanie zastaveného vypisovania,
- keď sa zaplní celá obrazovka, program skončí,
- program po skončení vypisovania napíše počet napísaných jednotiek a počet núl.
'''
##import tkinter,random
##canvas = tkinter.Canvas(width=400,height=400)
##canvas.pack()
##def animacia():
##    global x,y,pocet0,pocet1
##    cislo=random.randint(0,1)
##    if cislo==0:
##        farba='blue'
##        pocet0 = pocet0+1
##    else:
##        farba='green'
##    pocet1 = pocet1+1
##    canvas.create_text(x,y,text=cislo,fill=farba)
##    x = x+10
##    if x>80:
##        x = 10
##        y = y+10
##    if y<390 and pauza==0:
##        canvas.after(10,animacia)
##    if y>=390:
##        print('Počet 0:',pocet0)
##        print('Počet 1:',pocet1)
##def stlacilp(event):
##    global pauza
##    if pauza==1:
##        pauza=0
##        canvas.after(100,animacia)
##    else:
##        pauza=1
##x = 10
##y = 10
##pocet0 = 0
##pocet1 = 0
##pauza = 0
##canvas.create_text(300,350,text='stlač \'p\' pre pauzu')
##canvas.bind_all('p',stlacilp)
##animacia()

'''
Vytvorte program, ktorý bude mať tieto vlastnosti:
- z ľavého okraja sa pohybuje vo vodorovnom smere modrá gulička,
- z pravého okraja sa pohybuje vo vodorovnom smere k ľavej strane červená gulička,
- v každom kroku posunu si guličky (každá zvlášť) určia veľkosť posunu od 5 do 10 pixelov,
- animácia sa zastaví, keď sa loptičky stretnú,
- v mieste stretu sa niečo vypíše, napríklad BUM,
- animácia bude naprogramovaná v jednej funkcii (použite len jeden časovač).

'''
##import tkinter, random
##canvas = tkinter.Canvas(width = 400, height = 300)
##canvas.pack()
##
##canvas.pack()
##def animacia():
##    global x1,x2
##    canvas.delete('all')
##    x1 = x1 + random.randint(5,10)
##    x2 = x2 - random.randint(5,10)
##    canvas.create_oval(x1-5,200,x1+5,210,fill='blue')
##    canvas.create_oval(x2-5,200,x2+5,210,fill='red')
##    if x1+5>=x2-5:
##        canvas.create_text(x1,190,text='BUM')
##    else:
##        canvas.after(100,animacia)
##x1=0
##x2=400
##animacia()
#------------------------------------------------------------







