import tkinter as tk
def print_text(text, textbox):
    textbox.set(text)

m = tk.Tk()
e1 = tk.Entry(m)
e1.pack()
for i in range(0,10):
    button = tk.Button(m, text=i, width=2, height=2 ,command= lambda:print_text(i,e1))
    button.pack()
m.mainloop()
