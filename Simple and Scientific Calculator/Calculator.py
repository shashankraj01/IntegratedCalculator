from Tkinter import *
import math
import tkMessageBox


top=Tk()
top.title("CALCULATOR")
top.geometry("550x600+30+30")


def x():
    top.destroy()
    import Standard_Calculator

def y():
    top.destroy()
    import Scientific_Calculator

def z():
    top.destroy()


photo=PhotoImage(file="img.ppm")
labela=Label(top,image=photo)

buttona=Button(top,text='STANDARD CALCULATOR',width=35,height=2,bg="black",fg="white",command=x)
buttonb=Button(top,text='SCIENTIFIC CALCULATOR',width=35,height=2,bg="black",fg="white",command=y)
buttonc=Button(top,text='QUIT',width=15,height=1,bg="red",fg="white",command=z)
buttona.place(x=150,y=150)
buttonb.place(x=150,y=250)
buttonc.place(x=400,y=50)
labela.pack()


top.mainloop()