from tkinter import*
from time import strftime

root=Tk()
root.title("Digital Clock")
label=Label(root,font=("sans",80),background="black",foreground="orange")
label.pack(anchor="center")

def clock():
    tick=strftime("%H:%M:%S %p")
    label.config(text=tick)
    label.after(1000,clock)
clock()
mainloop()