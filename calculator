import tkinter as tk
from tkinter.font import Font

def btns(num):#this function Handles the function when the button clicked
    text = num.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())  
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    
    elif text == "del":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)
#setting the window size 
window= tk.Tk()
window.title("Calculator")
window.geometry("250x400")
window.configure(bg="gray" )

# Create an input field (Entry widget) for displaying and inputting numbers and expressions
entry = tk.Entry(window, font=("typewriter", 20))
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=10) 

#buttons 
buttons = (
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    ".", "0", "=", "/",
    "del"
)

c = 0  # column
r = 1  # row
button_index = 0

while button_index < len(buttons):
    button_text = buttons[button_index]
    btn = tk.Button(window, text=button_text, font=("typewriter", 15), padx=10, pady=10, width=5, height=2)
    #grid helps to the buttons to place in their respective rows and columns
    btn.grid(row=r, column=c, padx=5, pady=5)
    c += 1
    if c > 3:
        c = 0
        r += 1
    button_index += 1

row_index = 1
while row_index < 6:
    window.grid_rowconfigure(row_index, weight=1)
    row_index += 1

column_index = 0
while column_index < 4:
    window.grid_columnconfigure(column_index, weight=1)
    column_index += 1

child_index = 0
while child_index < len(window.winfo_children()):
    btn = window.winfo_children()[child_index]
    btn.bind("<Button-1>", btns)
    child_index += 1

window.mainloop()
