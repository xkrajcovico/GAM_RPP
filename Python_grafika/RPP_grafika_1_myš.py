'''
V programe môžeme reagovať aj na pohyb myši.
Pohyb myši bez zatlačeného tlačidla vyvolá udalosť s názvom
'<Motion>'.
Pohyb myši so zatlačeným ľavým tlačidlom vyvolá udalosť s názvom '<B1-Motion>'
a pravétlačidlo s pohybom '<B3-Motion>'.
Občas môžeme využiť aj udalosť '<ButtonRelease-1>' (uvoľnenie
zatlačeného ľavého tlačidla) alebo '<Double-Button-1>' (dvojklik).
'''

##import tkinter 
##canvas = tkinter.Canvas(width = 800, height = 600)
##canvas.pack() 
###krúžky a štvorce
##def kruzok(sur):
##        x = sur.x
##        y = sur.y
##        if x < 300:
##                canvas.create_oval(x, y, x+20, y+20, fill = 'blue')
##        else:
##                canvas.create_oval(x, y, x+20, y+20, fill = 'green')
##def stvorec(sur):
##        x = sur.x
##        y = sur.y
##        if y < 300:
##                canvas.create_rectangle(x, y, x+20, y+20, fill = 'red')
##        else:
##                canvas.create_rectangle(x, y, x+20, y+20, fill = 'yellow')
##canvas.bind('<Button-1>',kruzok)
##canvas.bind('<Button-3>',stvorec)
#-------------------------------------------------

#smajlík - klikanie
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
def smajlik(suradnice):
   x = suradnice.x
   y = suradnice.y
   canvas.create_oval(x-20,y-20,x+20,y+20, fill='green')
   canvas.create_oval(x-15,y-10,x-10,y-5)
   canvas.create_oval(x+15,y-10,x+10,y-5)
   canvas.create_text(x,y+10,text=')',angle=-90)
canvas.bind('<Button-1>',smajlik)


#smajlík
##import tkinter
##canvas = tkinter.Canvas()
##canvas.pack()
def smajlik(suradnice):
   x = suradnice.x
   y = suradnice.y
   canvas.create_oval(x-20,y-20,x+20,y+20, fill='yellow')
   canvas.create_oval(x-15,y-10,x-10,y-5)
   canvas.create_oval(x+15,y-10,x+10,y-5)
   canvas.create_text(x,y+10,text=')',angle=-90)
canvas.bind('<B1-Motion>',smajlik)


