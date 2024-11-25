import tkinter, random

canvas = tkinter.Canvas()
canvas.pack()

n1 = int(input(f'zadaj počet stĺpcov: '))
n2 = int(input(f'zadaj počet riadkov: '))
size = 20
f1 = str(input(f'zadaj prvú farbu: '))
f2 = str(input(f'zadaj druhú farbu: '))
print(n1,n2,f1,f2)

for i in range(n2):
        for j in range(n1):
            if i % 2 == 0 and j % 2 != 0 or i % 2 != 0 and j % 2 == 0:
                canvas.create_rectangle(size*(i+1),size*(j+1),size*(i+1)+size,size*(j+1)+size,fill = f1)
            else:
                canvas.create_rectangle(size*(i+1),size*(j+1),size*(i+1)+size,size*(j+1)+size,fill = f2)

canvas.mainloop()
