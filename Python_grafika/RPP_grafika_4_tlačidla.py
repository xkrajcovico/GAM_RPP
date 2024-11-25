'''
Nasledujúci program nám vytvorí dve vstupné polia
entry1 a entry2a dve tlačidlá button1a button2.
Do entry1  a  entry2 zadávame hodnoty, s ktorými vykonávame operácie,
ktoré máme zadefinované ako funkcie sucet() a rozdiel().
'''
import tkinter, random
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()
def sucet():
    a = int(entry1.get())
    b = int(entry2.get())
    print(a+b)
    canvas.create_text(100,100, text = 'súčet čísel je'+ str(a+b))
def rozdiel():
    a = int(entry1.get())
    b = int(entry2.get())
    print(a-b)
    canvas.create_text(100,200, text = 'rozdiel čísel je' + str(a-b))

entry1 = tkinter.Entry()
entry1.pack()
entry2 = tkinter.Entry()
entry2.pack()
button1 = tkinter.Button(text='súčet!',command=sucet)
button1.pack()
button2 = tkinter.Button(text='rozdiel!',command=rozdiel)
button2.pack()
