import tkinter, random

canvas = tkinter.Canvas()
canvas.pack()
out = ''
canvas.create_line(10,10,10,90,width = 5)
for i in range(10):
    cislo = random.randrange(1,9)
    canvas.create_line(10 + (12*(i+1)),10,10 + (12*(i+1)),80,width = cislo)
    canvas.create_text(10 + (12*(i+1)), 87, text = cislo)
    out += str(cislo)
canvas.create_line(8 + 15*i,10,8 + 15*i,90,width = 5)
print(f'cislo bar codu je: {out}')
canvas.mainloop()
