import turtle
t = turtle.Turtle()
pole = []

def klik(x,y):
    t.goto(x,y)
    pole.append([x,y])
    
def cisti(x,y):
    t.clear()
    
def kresli(x,y):
    t.setpos(x,y)
    for i in range(len(pole)):
        t.goto(pole[i])

    
screen=turtle.Screen()
screen.onclick(klik, btn = 1)
screen.onclick(cisti, btn = 3)
screen.onclick(kresli, btn = 2)
