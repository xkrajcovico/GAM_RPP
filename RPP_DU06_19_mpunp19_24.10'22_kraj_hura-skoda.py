import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()
sucet = 0
i,j = 0,0
k = int(input(f'zadaj cislo k: '))
for j in range(5):
    while sucet < k:
        canvas.create_oval(i*20,j*20,(i+1)*20,j*20 + 20)
        cislo = random.randrange(1,5)
        canvas.create_text(10+i*20,20*(j+0.5), text = str(cislo))
        i += 1
        sucet += cislo
    if sucet == k:
        canvas.create_text(10+i*22,20*(j+0.5), text = 'hura')
    else:
        canvas.create_text(10+i*22,20*(j+ 0.5), text = 'skoda')
    sucet,i = 0,0

tkinter.mainloop()

# def hra(k,sucet = 0):
# hra(k)
