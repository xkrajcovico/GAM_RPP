import tkinter, random
canvas = tkinter.Canvas(width = 600, height = 600)
canvas.pack()

circle = canvas.create_oval(x, 100, x+25, 125, fill = 'black' )
def posun():
    canvas.move(circle,1,0)
    
    if x > 300:
        canvas.create_text(10,10,text='skoncil som')
    canvas.after(3,posun)

posun()
canvas.mainloop()