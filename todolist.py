#Simple To_Do List app
#by TokyoEdtech
#Python 3.8 using Geany Editor
#Ubuntu Linux (Mac and Windows Compatible)
#Topics: tkinter , grid geometry manager
#Topics: Listbox Widget,Scrollbar Widget,tkinter.messagebox, Try/Except Block , pickle
import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List By Kavita")

def add_task():
    task = entry_task.get()
    if task !="":
        listbox_tasks.insert(tkinter.END , task)
        entry_task.delete(0 , tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!" , message="You must Enter a Task.")
       
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!" , message="You must Select a Task.")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat" , "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END,task)
    except:
        tkinter.messagebox.showwarning(title="Warning!" , message="Cannot find tasks.dat .")
                
        
    

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    
    pickle.dump(tasks, open("tasks.dat","wb"))   


#create gui
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()
listbox_tasks = tkinter.Listbox(frame_tasks , height=33, width=100)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT , fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root , width=100)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task" , width=100 , command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task" , width=100 , command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text="Load task" , width=100 , command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save tasks" , width=100 , command=save_tasks)
button_save_tasks.pack()

root.mainloop()