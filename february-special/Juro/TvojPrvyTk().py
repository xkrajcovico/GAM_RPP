import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
root = tk.Tk()
root.geometry('400x400')
root.title('stringprint')
root.resizable(False,False)
#########################################################################
# sem naprogramuj FUNKCIE
# podprogram printujuci string: 'congrats u clicked me'

def sprava():
    messagebox.showinfo("showinfo", "Fuck you")

# definicia py.button-u

clickme = ttk.Button(text = 'clickme', command = sprava)


nazov = tk.StringVar()
vstup = ttk.Entry(textvariable = nazov)
vstup.place(x = 100,y = 100)

def printstring():
    premenna = ttk.Label(text=vstup)
    premenna.place(x= 10,y= 10)



#########################################################################
# sem naprogramuj WIDGETY

clickme.place(x = 150,y= 150)








#########################################################################
root.mainloop()
