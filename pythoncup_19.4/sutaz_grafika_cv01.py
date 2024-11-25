# from turtle import *
# tina=Turtle()
# tina.shape("arrow")

# for i in range(52):
#     fillcolor('blue')
#     begin_fill()
#     tina.forward(20), tina.ht()
#     tina.right(10), tina.ht()
#     end_fill()
#     delay(10)
#     print(tina.heading())


# import turtle
# pole = []
# for i in range(5):
#  t = turtle.Turtle()
#  t.pu()
#  t.setpos(-300 + 100 * i, 0)
#  t.seth(90)
#  pole.append(t)
#  t._delay(0)
# #každá korytnačka nakreslí kružnicu
# #korytnačky kreslia postupne
# for i in range(24):
#     for t in pole:
#         t.pd()
#         t.fd(5)
#         t.lt(360/24)
#         t.pu()
#         t._delay(0)

# import turtle
# from random import randrange
# t = turtle.Turtle()
# for i in range(10000):
#     t.fd(randrange(5))
#     t.rt(randrange(-50,50))
#     t._delay(0)

# import turtle
# from random import randrange
# pole = []
# for i in range(20):
#  t = turtle.Turtle()
#  t.pu()
#  t.setpos(-30 + 10 * i, 0)
#  t.seth(90)
#  pole.append(t)
#  t._delay(0)
# #každá korytnačka nakreslí kružnicu
# #korytnačky kreslia postupne
# for i in range(100):
#     for t in pole:
#         t.pd()
#         t.fd(20)
#         if i%2:
#            t.rt(i*10)
#         else:
#            t.lt(i*10)
#         t.pu()
#         t._delay(0)

# import turtle
# def pohyb(x,y):
#  screen.tracer(0) #vypne kĺzanie korytnačky po jej trase
#  tina.goto(x,y)
#  screen.tracer(1) #zapne kĺzanie korytnačky po jej trase
# tina=turtle.Turtle()
# tina.shape("turtle")
# tina.shapesize(2,2,2)
# tina.color("yellow","green")
# tina.pensize(10)
# screen=turtle.Screen()
# screen.onclick(pohyb)

import turtle
t = turtle.Turtle()
t.up
def klik(x,y):
    t.goto(x,y)
screen=turtle.Screen()
screen.onclick(klik)
