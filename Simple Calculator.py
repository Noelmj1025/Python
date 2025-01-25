import tkinter as tk
from tkinter import messagebox
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def factorial(x):
    if x < 0:
        return "Error! Factorial does not exist for negative numbers."
    return math.factorial(x)

def root(x, n=2):
    if x < 0 and n % 2 == 0:
        return "Error! Cannot take even root of negative number."
    return x ** (1/n)

def update_display(text):
    entry_var.set(text)

def button_click(value):
    current = entry_var.get()
    if current == "Error!":
        update_display(value)
    else:
        update_display(current + str(value))

def calculate():
    try:
        result = eval(entry_var.get())
        update_display(result)
    except Exception as e:
        update_display("Error!")

def clear_display():
    update_display("")

def backspace():
    current = entry_var.get()
    if len(current) > 0:
        update_display(current[:-1])
    else:
        update_display("")

def calculate_factorial():
    try:
        number = int(entry_var.get())
        result = factorial(number)
        update_display(result)
    except ValueError:
        update_display("Error!")

def calculate_root():
    try:
        number = float(entry_var.get())
        degree = int(entry_var.get() or 2)
        result = root(number, degree)
        update_display(result)
    except ValueError:
        update_display("Error!")

root = tk.Tk()
root.title("Simple Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="sunken", width=20, justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('Clear', 5, 0), ('Back', 5, 1), ('Fact', 5, 2), ('Root', 5, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 15), width=5, height=2, command=calculate)
    elif text == "Clear":
        btn = tk.Button(root, text=text, font=("Arial", 15), width=5, height=2, command=clear_display)
    elif text == "Back":
        btn = tk.Button(root, text=text, font=("Arial", 15), width=5, height=2, command=backspace)
    elif text == "Fact":
        btn = tk.Button(root, text=text, font=("Arial", 15), width=5, height=2, command=calculate_factorial)
    elif text == "Root":
        btn = tk.Button(root, text=text, font=("Arial", 15), width=5, height=2, command=calculate_root)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 15), width=5, height=2, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col)

root.mainloop()
