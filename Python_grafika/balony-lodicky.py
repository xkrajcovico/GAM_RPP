import tkinter, random
canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()

farby1 = ['red','yellow','orange']
farby2 = ['green3','orangered','purple']
farby3 = ['forestgreen','gold3','dodgerblue']

canvas.create_rectangle(0,400,802,602, fill = 'royalblue2', outline='royalblue2')

def lodicka(x,y):              # lodicka
    # x = sur.x
    # y = sur.y
    canvas.create_line([x,y],[x,y-60], width=2)
    canvas.create_line([x-20,y],[x-40,y-10], width=2)
    canvas.create_polygon([x-20,y+5],[x-30,y-5],[x+30,y-5],[x+20,y+5])
    canvas.create_polygon([x+3,y-42],[x+3,y-60],[x+35,y-57.5],fill = random.choice(farby2), outline = 'black')
    canvas.create_polygon([x+3,y-7],[x+36,y-7],[x+32.5,y-15],[x+33,y-25],[x+36,y-55],[x+3,y-40],fill = random.choice(farby1), outline = 'black')
    canvas.create_polygon([x-20,y-7],[x-3,y-7],[x-5,y-27.5],[x-3.5,y-47.5],[x-3,y-57.5],fill = random.choice(farby2), outline = 'black')
    canvas.create_polygon([x-38,y-13],[x-24,y-6],[x-8,y-51.5],fill = random.choice(farby3), outline = 'black')
    

def balon(x,y):                # balon
    # x = sur.x
    # y = sur.y
    canvas.create_polygon([x-5,y+11],[x-10,y-5],[x+10,y-5],[x+5,y+11])
    canvas.create_line([x-10,y-5],[x-15,y-30], width=2)
    canvas.create_line([x+10,y-5],[x+15,y-30], width=2)
    canvas.create_line([x+3,y-5],[x+7.5,y-30], width=2) 
    canvas.create_line([x-3,y-5],[x-7.5,y-30], width=2)
    canvas.create_oval([x-20,y-66],[x+20,y-22],fill = random.choice(farby1))
    canvas.create_oval([x-12,y-66],[x+12,y-22],fill = random.choice(farby2))
    canvas.create_oval([x-5,y-66],[x+5,y-22],fill = random.choice(farby3))


def lodicka_alebo_balon(sur):
    x = sur.x
    y = sur.y
    if y > 395:
        lodicka(x,y)
    else:
        balon(x,y)

canvas.bind('<Button-1>',lodicka_alebo_balon)
# canvas.bind('<Button-3>',balon)


canvas.mainloop()


# import tkinter as tk
# root = tk.Tk()

# def motion(event):
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))

# root.bind('<Motion>', motion)
# root.mainloop()