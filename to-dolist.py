import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def toggle_task():
    try:
        index = listbox.curselection()
        task_text = listbox.get(index)
        if task_text.startswith("✓ "):
            task_text = task_text[2:]
        else:
            task_text = "✓ " + task_text
        listbox.delete(index)
        listbox.insert(index, task_text)
    except:
        messagebox.showwarning("Warning", "Please select the task you've done.")


window = tk.Tk()
window.title("To-Do List")
window.configure(bg="grey") 

# Create an entry widget to add tasks
entry = tk.Entry(window, width=50)
entry.pack(padx=10, pady=5, side=tk.TOP)  

# Create a frame to hold the buttons
button_frame = tk.Frame(window, bg="pink")
button_frame.pack(padx=10, pady=5)


button_font = Font(family="Arial", size=12, weight="bold")

# an "Add Task" button
add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=button_font)
add_button.pack(side=tk.LEFT, padx=5)

# a "Delete Task" button
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=button_font)
delete_button.pack(side=tk.LEFT, padx=5)

# a "Done Task" button
toggle_button = tk.Button(button_frame, text="Done Task", command=toggle_task, font=button_font)
toggle_button.pack(side=tk.LEFT, padx=5)

# a listbox to display tasks
listbox = tk.Listbox(window, width=50)
listbox.pack(padx=10, pady=5)

# a scrollbar for the listbox
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link the scrollbar to the listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Start the Tkinter event loop
window.mainloop()
