from tkinter import *
root = Tk()
labelarray = []
e = Entry(root, width=36)
e.grid(row=0,column=0,columnspan=4)

def a1():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + "1")
def a2():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + "2")
def a3():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + "3")
def a4():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + "4")
def a5():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + "5")
def a6():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + "6")
def a7():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + "7") 
def a8():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + "8")
def a9():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + "9")
def a0():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + "0")

    
def aadd():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + "+")
def adiff():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + "-")
def amul():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + "*")
def adiv():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + "/")
def alp():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + "(")
def arp():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + ")")
def adp():
    cr = e.get()
    e.delete(0, END)
    e.insert(0,str(cr) + ".")

    
def ae():
    a=e.get()
    e.delete(0, END)
    e.insert(0, eval(a))
def aAC():
    e.delete(0, END)
def acl():
    a=e.get()
    e.delete(0, END)
    e.insert(0, a[0:len(a)-1])
    
def getbutton(labelvar,cmdvar):
    return Button(root, text=labelvar, padx=20, pady=20, command=cmdvar)

Bttn1 = Button(root, text="1", padx=20, pady=20, command=a1)
Bttn2 = Button(root, text="2", padx=20, pady=20, command=a2)
Bttn3 = Button(root, text="3", padx=20, pady=20, command=a3)
Bttn4 = Button(root, text="4", padx=20, pady=20, command=a4)
Bttn5 = Button(root, text="5", padx=20, pady=20, command=a5)
Bttn6 = Button(root, text="6", padx=20, pady=20, command=a6)
Bttn7 = Button(root, text="7", padx=20, pady=20, command=a7)
Bttn8 = Button(root, text="8", padx=20, pady=20, command=a8)
Bttn9 = Button(root, text="9", padx=20, pady=20, command=a9)
Bttn0 = Button(root, text="0", padx=20, pady=20, command=a0)

Bttne = Button(root, text="=", padx=20, pady=20, command=ae)
BttnAC = Button(root, text="AC", padx=16, pady=20, command=aAC)
Bttncl = Button(root, text="<-", padx=16, pady=20, command=acl)

Bttnadd = Button(root, text="+", padx=20, pady=20, command=aadd)
Bttndiff = Button(root, text="-", padx=20, pady=20, command=adiff)
Bttnmul = Button(root, text="*", padx=20, pady=20, command=amul)
Bttndiv = Button(root, text="/", padx=20, pady=20, command=adiv)
Bttndp = Button(root, text=".", padx=20, pady=20, command=adp)
Bttnlp = Button(root, text="(", padx=20, pady=20, command=alp)
Bttnrp = Button(root, text=")", padx=20, pady=20, command=arp)

BttnAC.grid(row=1,column=0)
Bttncl.grid(row=1,column=1)
Bttnlp.grid(row=1,column=2)
Bttnrp.grid(row=1,column=3)


Bttn7.grid(row=2,column=0)
Bttn8.grid(row=2,column=1)
Bttn9.grid(row=2,column=2)
Bttnadd.grid(row=2,column=3)


Bttn4.grid(row=3,column=0)
Bttn5.grid(row=3,column=1)
Bttn6.grid(row=3,column=2)
Bttndiff.grid(row=3,column=3)


Bttn1.grid(row=4,column=0)
Bttn2.grid(row=4,column=1)
Bttn3.grid(row=4,column=2)
Bttnmul.grid(row=4,column=3)


Bttn0.grid(row=5,column=0)
Bttndp.grid(row=5,column=1)
Bttne.grid(row=5,column=2)
Bttndiv.grid(row=5,column=3)

root.mainloop()



