import tkinter
import tkinter.messagebox
import pickle # added this line

window=tkinter.Tk()
window.title("TO DO LIST")
list_frame=tkinter.Frame(window)
list_frame.pack()
def task_adding():
    todo=task_add.get()
    if todo != '':
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention !!",message="To add a task,please  enter some task")
def task_remove():
    try:
        index_todo=todo_box.curselection()[0] # changed list_frame to todo_box
        todo_box.delete(index_todo) # changed list_frame to todo_box
    except:
        tkinter.messagebox.showwarning(title="Attention !!",message="To delete a task,please select a task")
def task_load():
    try:
        todo_list = pickle.load(open("tasks.dat","rb"))
        todo_box.delete(0,tkinter.END) # changed list_frame to todo_box
        for task in todo_list:
            todo_box.insert(tkinter.END,task) # changed todo to task
    except:
        tkinter.messagebox.showwarning(title="Attention !!",message="Cannot find tasks.dat")
def task_save():
    todo_list = todo_box.get(0,tkinter.END) # changed list_frame to todo_box
    pickle.dump(todo_list,open("tasks.dat","wb"))


todo_box=tkinter.Listbox(list_frame,height=20,width=50)
todo_box.pack(side=tkinter.LEFT)
scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT,fill=tkinter.Y)
todo_box.config(yscrollcommand=scroller.set)
#scroller.config(command=list_frame.yview) 
task_add=tkinter.Entry(window,width=50)
task_add.pack()
add_task_button = tkinter.Button(window,text="ADD THE TASK",font=("arial",20,"bold"),bg="light green",width=20,command=task_adding)
add_task_button.pack()
remove_task_button = tkinter.Button(window,text="REMOVE THE TASK",font=("arial",20,"bold"),bg="sky blue",width=20,command=task_remove)
remove_task_button.pack()
save_task_button = tkinter.Button(window,text="CLICK TO SAVE",font=("arial",20,"bold"),bg="red",width=20,command=task_save) # removed parentheses
save_task_button.pack()

load_task_button=tkinter.Button(window,text="LOAD THE TASK",font=("arial",20,"bold"),bg="yellow",width=20,command=task_load) # removed parentheses
load_task_button.pack()

window.mainloop()
