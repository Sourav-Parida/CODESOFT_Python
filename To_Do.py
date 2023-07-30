from tkinter import *
from tkinter import messagebox

def newTask():
    task = entered_task.get()
    if task != "":
        lb.insert(END, task)
        entered_task.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    
root = Tk()
root.geometry('400x400')
root.title('PythonGuides')
root.config(bg='light blue')
root.resizable(width=False, height=False)

frame = Frame(root)
frame.pack(pady=8)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=1,
    fg='#464646',
    highlightthickness=0,
    selectbackground='gray',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    ' DSA Homework',
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

entered_task = Entry(
    root,
    font=('times', 24)
    )

entered_task.pack(pady=18)

button_frame = Frame(root)
button_frame.pack()

addtask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addtask_btn.pack(fill=BOTH, expand=True, side=LEFT)

deltask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
deltask_btn.pack(fill=BOTH, expand=True, side=LEFT)


root.mainloop()