import turtle
t = turtle.Turtle()
pole = []

def klik(x,y):
    t.goto(x,y)
    pole.append([x,y])
    
def cisti(x,y):
    t.clear()
    
def kresli(x,y):
    t.pu()
    t.setpos(x,y)
    t.pd()
    out = []
    for i in range(len(pole)):
        out.append([pole[i][0]+x,pole[i][1]+y])
    for i in range(len(out)):
        t.goto(out[i])

    
screen=turtle.Screen()
screen.onclick(klik, btn = 1)
screen.onclick(cisti, btn = 3)
screen.onclick(kresli, btn = 2)
