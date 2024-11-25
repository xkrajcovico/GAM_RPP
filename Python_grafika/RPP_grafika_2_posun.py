'''
mám nakreslené štyri útvary (text, rectangle, line, oval)
'''

##import tkinter
##canvas = tkinter.Canvas()
##canvas.pack()
##canvas.create_text(200,200,text='nadpis')
##canvas.create_rectangle(100,100,150,200,fill='red')
##canvas.create_line(50,50,200,150,width=5,fill='blue')
##canvas.create_oval(200,100,300,150,fill='green')


'''
- tieto objekty majú svoje čísla (text je 1, rectangle 2 atď
- môžem ich posúvať príkazom canvas.move(1,10,20)
To znamená:
- posunie mi prvý objekt (text)
- o +10  bodov na osi x 
- o +20 bodov na osi y
'''
#canvas.move(1,10,20)



'''
objektom môžem dať aj mená- napr.oval
oval = canvas.create_oval(200,100,300,150,fill='green')

Potom meno môžem použiť. 
Napríklad

canvas.move(oval, 30, -15)

posunie oval
- o +30  bodov na osi x 
- o -15 bodov na osi y
(čiže vpravo a hore).
'''

##import tkinter
##canvas = tkinter.Canvas()
##canvas.pack()
##oval = canvas.create_oval(200,100,300,150,fill='green')
##canvas.move(oval, 30, -15)


'''
Na udalosti stlačenia klávesu reagujeme
príkazom canvas.bind_all('kláves', funkcia).
Kláves je
konkrétny znak na klávesnici, napr. 'a' alebo 'd',
alebo názov ovládacieho klávesu. Napríklad môžeme
používať tieto klávesy:
'<Up>' – šípka hore,
'<Down>' – šípka dole,
'<Right>' – šípka vpravo,
'<Left>' – šípka vľavo,
Parameter funkcia je názov funkcie, ktorá sa vykoná.
Volaná funkcia však musí mať jeden parameter,
napríklad event (udalosť),
v ktorom sa funkcii pošlú podrobnejšie informácie o udalosti.
Rovnako ako pri
kliknutí myši aj pri stlačení klávesu sa posielajú v parametri súradnice
aktuálnej pozície myši.
Aj keď s týmto parametrom nepracujeme v našej funkcii,
musíme ho zadať pri definovaní funkcie
'''


import tkinter
canvas = tkinter.Canvas()
canvas.pack()

oval = canvas.create_oval(200,100,300,150,fill='green')

def posun(event):
    canvas.move(oval, 30, -15)
    
canvas.bind_all('<Right>',posun)

#Úloha
#dopíšte funkciu posun_vlavo(event), posun_hore(event), posun_dolu(event)
#ktorá bude posúvať VŠETKY objekty

##import tkinter
##canvas = tkinter.Canvas()
##canvas.pack()
##
##nadpis = canvas.create_text(200,200,text='nadpis')
##obdlznik = canvas.create_rectangle(100,100,150,200,fill='red')
##ciara = canvas.create_line(50,50,200,150,width=5,fill='blue')
##oval = canvas.create_oval(200,100,300,150,fill='green')
##
##def posun_vpravo(event):
##    canvas.move(nadpis, 5, 0)
##    canvas.move(obdlznik, 5, 0)
##    canvas.move(ciara, 5, 0)
##    canvas.move(oval, 5, 0)
##    
##def posun_vlavo(event):
##    pass
##def posun_hore(event):
##    pass
##def posun_dolu(event):
##    pass
##                
##canvas.bind_all('<Right>',posun_vpravo)
##canvas.bind_all('<Left>',posun_vlavo)
##canvas.bind_all('<Up>',posun_hore)
##canvas.bind_all('<Down>',posun_dolu)
##




