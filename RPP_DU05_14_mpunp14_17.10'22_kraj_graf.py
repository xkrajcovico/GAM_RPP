import tkinter, random

canvas = tkinter.Canvas()
canvas.pack()

vstup = 0
cislo =[]
while vstup != -1:
    vstup = int(input(f'zadaj cislo: '))
    if vstup != -1:
        cislo.append(vstup)


for i in  range(len(cislo)+1):
    canvas.create_rectangle((10+ 25*(i-1)),200 - (cislo[i-1]), 25 +25*(i-1),200,fill = 'cyan')
for i in  range (len(cislo)):
    canvas.create_text((16+ 25.5*i),220,text = cislo[i])
