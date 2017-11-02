from Tkinter import *
import math
import tkMessageBox


def a():
    root.destroy()
    import Calculator
    from Calculator import photo

def eleven():
    entry2.insert(END,"+")

def twelve():
    entry2.insert(END,"-")

def thirteen():
    entry2.insert(END,"X")

def fourteen():
    entry2.insert(END,"/")

def fifteen():
    entry2.insert(END,"MODULUS")

def sixteen():
    entry2.insert(END,"PERCENTAGE")

def seventeen():
    entry2.insert(END,"POWER")

def eighteen():
    entry2.insert(END,"SQRT")

def nineteen():
    entry2.insert(END,"RECIPROCAL")

def twenty():
    entry2.insert(END,"=")


def one():
    if(entry2.get()==''):
        entry1.insert(END,"1")
    else:
        entry3.insert(END,"1")

def two():
    if (entry2.get() == ''):
        entry1.insert(END, "2")
    else:
        entry3.insert(END, "2")

def three():
    if (entry2.get() == ''):
        entry1.insert(END, "3")
    else:
        entry3.insert(END, "3")

def four():
    if (entry2.get() == ''):
        entry1.insert(END, "4")
    else:
        entry3.insert(END, "4")

def five():
    if (entry2.get() == ''):
        entry1.insert(END, "5")
    else:
        entry3.insert(END, "5")

def six():
    if (entry2.get() == ''):
        entry1.insert(END, "6")
    else:
        entry3.insert(END, "6")

def seven():
    if (entry2.get() == ''):
        entry1.insert(END, "7")
    else:
        entry3.insert(END, "7")

def eight():
    if (entry2.get() == ''):
        entry1.insert(END, "8")
    else:
        entry3.insert(END, "8")

def nine():
    if (entry2.get() == ''):
        entry1.insert(END, "9")
    else:
        entry3.insert(END, "9")

def zero():
    if (entry2.get() == ''):
        entry1.insert(END, "0")
    else:
        entry3.insert(END, "0")

def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)

def allf():
    if(entry2.get()=='+'):
        a=int(entry1.get())+int(entry3.get())
        entry4.delete(0,END)
        entry4.insert(0,str(a))

    elif(entry2.get() == '-'):
        a=int(entry1.get())-int(entry3.get())
        entry4.delete(0, END)
        entry4.insert(0, str(a))

    elif (entry2.get() == '/'):
        a=float(entry1.get())/float(entry3.get())
        entry4.delete(0, END)
        entry4.insert(0, str(a))

    elif (entry2.get() == 'X'):
        a=float(entry1.get())*float(entry3.get())
        entry4.delete(0, END)
        entry4.insert(0, str(a))

    elif(entry2.get() == 'PERCENTAGE'):
        a=(float(entry1.get())/float(entry3.get()))*100
        entry4.delete(0, END)
        entry4.insert(0, str(a))
    elif(entry2.get() == 'MODULUS'):
        a=int(entry1.get())%int(entry3.get())
        entry4.delete(0, END)
        entry4.insert(0, str(a))

    elif(entry2.get() == 'POWER'):
        a=int(entry1.get())**int(entry3.get())
        entry4.delete(0, END)
        entry4.insert(0, str(a))
    elif(entry2.get() == 'SQRT'):
        a=math.sqrt(int(entry1.get()))
        entry4.delete(0, END)
        entry4.insert(0, str(a))
    elif(entry2.get() == 'RECIPROCAL'):
        a=1/float(entry1.get())
        entry4.delete(0, END)
        entry4.insert(0, str(a))
    else:
        tkMessageBox.showinfo("ERROR","Choose Correct Operation")

#****************FRAME**********************

root=Tk()

def standard():
    root=Tk()
    root.geometry("550x600+30+30")


menubar=Menu(root)
root.config(menu=menubar)

submenu=Menu(menubar)
menubar.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New",command=a)
submenu.add_separator()
submenu.add_command(label="save as",command=open)

editmenu=Menu(menubar)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=open)

frame2=Frame(root,height=50)
label=Label(frame2,text="STANDARD CALCULATOR")
label.pack()
frame2.pack(side=TOP,fill=X)

frame1=Frame(root,height=600,width=550)
frame1.pack()


#****************LABEL**********************

label1=Label(frame1,text="1. ENTER FIRST NUMBER :")
label2=Label(frame1,text="3. ENTER SECOND NUMBER :")
label3=Label(frame1,text="2. CHOOSE OPERATION :")
label4=Label(frame1,text="ANSWER:")

#****************ENTRY**********************


entry1=Entry(frame1,bd=5)
entry2=Entry(frame1,bd=5)
entry3=Entry(frame1,bd=5)
entry4=Entry(frame1,bd=5)

#****************PLACING**********************

label1.place(x=140,y=40)
label2.place(x=120,y=110)
label3.place(x=140,y=75)
label4.place(x=220,y=145)
entry1.place(x=300,y=40)
entry3.place(x=300,y=110)
entry2.place(x=300,y=75)
entry4.place(x=300,y=145)

#****************BUTTON**********************

button1=Button(frame1,text='+',command=eleven,bd=4,bg="cyan")
button2=Button(frame1,text='-',command=twelve,bd=4,bg="cyan")
button3=Button(frame1,text='X',command=thirteen,bd=4,bg="cyan")
button4=Button(frame1,text='/',command=fourteen,bd=4,bg="cyan")
button5=Button(frame1,text='Mod',command=fifteen,bd=4,bg="cyan")
button6=Button(frame1,text='%',command=sixteen,bd=4,bg="cyan")
button7=Button(frame1,text='POW',command=seventeen,bd=4,bg="cyan")
button8=Button(frame1,text='ROOT',command=eighteen,bd=4,bg="cyan")
button9=Button(frame1,text='1/x',command=nineteen,bd=4,bg="cyan")
button10=Button(frame1,text='0',command=zero,bd=4,bg="coral")
button11=Button(frame1,text='1',command=one,bd=4,bg="coral")
button12=Button(frame1,text='2',command=two,bd=4,bg="coral")
button13=Button(frame1,text='3',command=three,bd=4,bg="coral")
button14=Button(frame1,text='4',command=four,bd=4,bg="coral")
button15=Button(frame1,text='5',command=five,bd=4,bg="coral")
button16=Button(frame1,text='6',command=six,bd=4,bg="coral")
button17=Button(frame1,text='7',command=seven,bd=4,bg="coral")
button18=Button(frame1,text='8',command=eight,bd=4,bg="coral")
button19=Button(frame1,text='9',command=nine,bd=4,bg="coral")
button20=Button(frame1,text='=',command=allf,bd=4,bg="dimgrey")
button21=Button(frame1,text="BACK",bd=3,bg="teal",command=a)
button22=Button(frame1,text="QUIT",command=root.quit,bd=3,bg="red")
button23=Button(frame1,text='CLEAR',command=clear,bd=4,bg="white")
#********************PLACING********************

button1.place(x=20,y=200,height=40,width=90)
button2.place(x=150,y=200,height=40,width=90)
button3.place(x=280,y=200,height=40,width=90)
button4.place(x=410,y=200,height=40,width=90)
button5.place(x=410,y=275,height=40,width=90)
button6.place(x=410,y=350,height=40,width=90)
button7.place(x=410,y=425,height=40,width=90)
button8.place(x=410,y=500,height=40,width=90)
button9.place(x=20,y=500,height=40,width=90)
button10.place(x=150,y=500,height=40,width=90)
button11.place(x=20,y=275,height=40,width=90)
button12.place(x=150,y=275,height=40,width=90)
button13.place(x=280,y=275,height=40,width=90)
button14.place(x=20,y=350,height=40,width=90)
button15.place(x=150,y=350,height=40,width=90)
button16.place(x=280,y=350,height=40,width=90)
button17.place(x=20,y=425,height=40,width=90)
button18.place(x=150,y=425,height=40,width=90)
button19.place(x=280,y=425,height=40,width=90)
button20.place(x=280,y=500,height=40,width=90)
button21.place(x=10,y=40,height=30,width=80)
button22.place(x=450,y=40,height=30,width=80)
button23.place(x=450,y=90,height=30,width=80)


root.mainloop()