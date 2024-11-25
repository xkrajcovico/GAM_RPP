import tkinter (as tk)
(from tkinter import ttk) – pre krajšie widgety

root = tk.Tk()
root.geometry('XxY‘)
(root.resizable(False, False)) – ak chceme aby užívateľ nemohol meniť 					veľkosť okna
jadro tvojho kódu

root.mainloop()


textik = ttk.Label(text = 'string‘,
                    fg = 'farbatextu‘
                    bg = 'farbapozadia')

tlacidlo = ttk.Button(text = 'string‘,
                        command = 'funkcia',
                        fg = 'farbatextu‘
                        bg = 'farbapozadia‘)

slider = ttk.Scale(from_ = ‚spodnahodnota,
                    to = 'vrchnahodnota‘,
                    orient = 'horizontal/vertical‘,
                    variable = 'nazov‘,
                    command = 'funkcia‘)

vstup = ttk.Entry(textvariable = 'nazov')

okienko = ttk.Checkbutton(text = 'string',
                            command = 'funkcia',
                            variable = 'nazov',
                            onvalue = 'hodnota',
                            offvalue = 'hodnota‘)

sprava = messagebox.showinfo("showinfo", "Information")
                    messagebox.showwarning("showwarning", "Warning")  
                    messagebox.showerror("showerror", "Error")  
                    messagebox.askquestion("askquestion", "Are you sure?")  
                    messagebox.askokcancel("askokcancel", "Want to continue?")  
                    messagebox.askyesno("askyesno", "Find the value?")  
                    messagebox.askretrycancel("askretrycancel", "Try again?") 
nazov_premennej_widgetu.place(x = 'xova', y = 'ypsilonova‘)
ak mám: command = mojafunkcia tak funkcia 'mojafunkcia' musí byť definovaná: def mojafunkcia():
https://www.tutorialspoint.com/python/python_gui_programming.htm 



