import turtle
t = turtle.Turtle()
t.up

def obdlznik(a,b):
        t.fd(a)
        t.right(90)
        t.fd(b)
        t.right(90)
        t.fd(a)
        t.right(90)
        t.fd(b)
        t.right(90)
        t.fd(a)
def slnko(n,strana,luc):
    for i in range(n):
        t._delay(0)
        obdlznik(strana,luc)
        t.left(360/n)
slnko (15,20,80)