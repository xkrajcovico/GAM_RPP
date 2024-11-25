# setup
import tkinter
from math import sqrt

canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()


a = [500,500]                                                   # coordinates for a and a
b = [505,505]

k =  50 #int(input())                                           # disctance between b and c

for i in range(35):
    ab = [ b[0] - a[0] , b[1] - a[1] ]                          # vector ab
    dlzka = sqrt((ab[0]**2) + (ab[1]**2))                       # distance between a and b
    n = [ab[1],-ab[0]]                                          # normal vector - ab --> n   

    c = (b[0] + (n[0]/(dlzka)*k) , b[1] + (n[1]/(dlzka)*k))     #point c; bc is perpendicular to ab, distance bc is k times smaller than ab

    canvas.create_line(b,c)                                     # connecting actual points
    canvas.create_line(a,c)

    b = c   # loop goes on...

canvas.mainloop()
# Made by: Ondrej Krajčovič 14.1.'23