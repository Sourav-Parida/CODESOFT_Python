from tkinter import *

def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if svalue.get().isdigit():
            value=int(svalue.get())
        else:
            try:
                value= eval(screen.get())
            except Exception as e:
                print(e)
                svalue.set("Error")
                screen.update()
        svalue.set(value)
        screen.update()

    elif text == "C":
        svalue.set("")
        screen.update()
    else:
        svalue.set(svalue.get() + text)
        screen.update()
#Sourav Parida

root = Tk()
root.config(bg="Gray30")

root.geometry("500x700")
root.title("Calculator")

svalue = StringVar()
svalue.set("")
screen = Entry(root,textvar=svalue, font='lucid 40 bold')
screen.pack(ipadx=10,pady=10,padx=10)

f = Frame(root,bg="Gray30")
b=Button(f,text="C",padx=13,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="C",padx=13,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="%",padx=10,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="/",padx=18,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="Gray30")
b=Button(f,text="7",padx=17,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=8)
b.bind("<Button-1>",click)
b=Button(f,text="8",padx=17,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=8)
b.bind("<Button-1>",click)
b=Button(f,text="9",padx=17,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=8)
b.bind("<Button-1>",click)
b=Button(f,text="*",padx=16,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=8)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="Gray30")
b=Button(f,text="4",padx=17,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="5",padx=17,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="6",padx=17,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="-",padx=17,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="Gray30")
b=Button(f,text="1",padx=17,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="2",padx=17,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="3",padx=17,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="+",padx=11,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="Gray30")
b=Button(f,text="0",padx=17,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="00",padx=6,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text=".",padx=21,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="=",padx=12,font="lucida 33 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)
f.pack()




root.mainloop()

