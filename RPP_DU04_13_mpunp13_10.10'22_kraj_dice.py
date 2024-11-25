import tkinter, random

canvas = tkinter.Canvas()
canvas.pack()
colours = ["orange","cyan","magenta","red","blue", 'lime',"yellow"]

import random
dice = []
sucet = 0
cislo = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(100):
    for i in range(2):
        nahoda = random.randrange(6)
        sucet += nahoda
    if sucet == 2:
        cislo[0] += 1
    elif sucet == 3:
        cislo[1] += 1
    elif sucet == 4:
        cislo[3] += 1
    elif sucet == 5:
        cislo[4] += 1
    elif sucet == 6:
        cislo[5] += 1
    elif sucet == 7:
        cislo[6] += 1
    elif sucet == 8:
        cislo[7] += 1
    elif sucet == 9:
        cislo[8] += 1
    elif sucet == 10:
        cislo[9] += 1
    elif sucet == 11:
        cislo[10] += 1
    elif sucet == 12:
        cislo[11] += 1
    sucet = 0

for i in  range(12):
    canvas.create_rectangle((10+ 25*(i-1)),200 - (cislo[i-1]*5), 25 +25*(i-1),200,fill = colours[random.randrange(0,len(colours))]) #
for i in  range(11):
    canvas.create_text((16+ 25.5*i),220,text = i+2)
