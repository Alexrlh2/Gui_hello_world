from tkinter import *
from tkinter import ttk



def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(round(value * 0.3048, 3))
    except ValueError:
        meters.set('Error')


root = Tk()
root.title('Feet to Meters')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(row=2, column=2, sticky=(W, E))

ttk.Button(mainframe, text='Calculate', command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text='Meters').grid(column=3, row=2, stick=W)
ttk.Label(mainframe, text='are equivalent to').grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text='Feet').grid(column=3, row=1, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
