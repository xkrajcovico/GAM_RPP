import tkinter
from time import sleep
from random import randrange
canvas = tkinter.Canvas(width=500, height= 500)
canvas.pack()

def destroy():
    canvas.delete(img1)
    canvas.delete(super)

def klik(event): 
    x = event.x 
    y = event.y
    if (x >= sur[0]-25 and x <= sur[0]+25) and (y >= sur[1]-25 and y <= sur[1]+25):
        global body
        body += 1

m = randrange(3,6)
n = randrange(3,8)
global body
body = 0

for i in range(n):
    for j in range(m):
        if randrange(2) == 0:
            canvas.create_rectangle(i*50,j*50,i*50+50,j*50+50)
        else:
            canvas.create_rectangle(i*50,j*50,i*50+50,j*50+50, fill = 'lightgrey')

obrazok = tkinter.PhotoImage(file = "C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/pythoncup_krajcovic_19.4/duch.png")

for i in range(1):
    x,y = randrange(n)*50+25,randrange(m)*50+25
    img1 = canvas.create_image(x,y,image = obrazok)
    if body >=1:
        super = canvas.create_text(x+30,y-10, text = 'SUPER')
        break
    sur = [x,y]
    canvas.after(1000,destroy)



canvas.bind("<Button-1>",klik)


canvas.mainloop()
print(body)