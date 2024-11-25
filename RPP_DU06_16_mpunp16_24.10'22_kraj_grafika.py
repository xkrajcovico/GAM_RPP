import tkinter, random

canvas = tkinter.Canvas()
canvas.pack()
n = int(input(f'sem zadaj pocet bankoviek:'))
out = 0
cena = [1, 2, 5, 10, 20, 50, 100, 200, 500]

for i in range(n):
    cislo = random.randrange(8)
    canvas.create_rectangle(25,20*(i+1)+20,75,20)
    canvas.create_text(50,20*(i+1)+10,text = f'{cena[cislo]} €')
    out += int(cena[cislo])
canvas.create_text(200,50,text = f'spolu: {out} €')
canvas.mainloop()