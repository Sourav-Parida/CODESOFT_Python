from tkinter import *
import string
import random

def Generator():
    small=string.ascii_lowercase
    capital=string.ascii_uppercase
    num=string.digits
    special=string.punctuation
    all=small+capital+num+special

    passlen=int(length_box.get())
    password=random.sample(all,passlen)

    svalue.set(password)
    passfield.update()



root=Tk()
#root.geometry("500x700")
#root.config(bg="Blue")

root.title("Password Generator")

passwordlabel=Label(root,text='Password Generator',font=("times new roman",20,'bold'))
passwordlabel.grid(pady=10,padx=10)

length=Label(root,text='Password Length',font=("times new roman",17,'bold'))
length.grid()

length_box = Spinbox(root,from_=8,to_=18,width=5,font=(20))
length_box.grid()

generateBtn=Button(root,text='Generate',font=frozenset,command=Generator)
generateBtn.grid(pady=5)

svalue = StringVar()
svalue.set("")
passfield=Entry(root,textvar=svalue,width=20,bd=2,font=25)
passfield.grid(pady=20)


root.mainloop()