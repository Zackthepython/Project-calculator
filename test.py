import tkinter as tk
def print_text(text, textbox):
    textbox.set(text)

m = tk.Tk()
e1 = tk.Entry(m)
e1.pack()
for i in range(0,10):
    button = tk.Button(m, text=i, width=2, height=2 ,command= lambda:print_text(i,e1))
    button.pack(0,10)

    root.title("")

# Create three buttons
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
button3 = tk.Button(root, text="Button 3")

# Pack the buttons vertically
button1.pack()
button2.pack()
button3.pack()







m.mainloop()