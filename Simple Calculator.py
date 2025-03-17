import tkinter as tk
import math

# Mathematical operations
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
    if x < 0 or not x.is_integer():
        return "Error! Factorial is for non-negative integers."
    return math.factorial(int(x))

def root(x, n=2):
    if x < 0 and n % 2 == 0:
        return "Error! Cannot take even root of negative number."
    return x ** (1/n)

# Update the display
def update_display(text):
    entry_var.set(text)

# Append input to the display
def button_click(value):
    current = entry_var.get()
    if current == "Error!":
        update_display(value)
    else:
        update_display(current + str(value))

# Safer evaluation function
def safe_evaluate(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {"math": math, "sqrt": math.sqrt})
        return result
    except:
        return "Error!"

# Calculate result
def calculate():
    result = safe_evaluate(entry_var.get())
    update_display(result)

# Clear display
def clear_display():
    update_display("")

# Backspace function
def backspace():
    current = entry_var.get()
    update_display(current[:-1] if current else "")

# Factorial calculation
def calculate_factorial():
    try:
        number = float(entry_var.get())
        result = factorial(number)
        update_display(result)
    except ValueError:
        update_display("Error!")

# Square root calculation
def calculate_root():
    try:
        number = float(entry_var.get())
        result = root(number, 2)  # Default to square root
        update_display(result)
    except ValueError:
        update_display("Error!")

# Create GUI window
root = tk.Tk()
root.title("Simple Calculator")
root.resizable(False, False)

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="sunken", width=20, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('Clear', 5, 0), ('Back', 5, 1), ('Fact', 5, 2), ('√', 5, 3),
]

for (text, row, col) in buttons:
    command = None
    if text == "=":
        command = calculate
    elif text == "Clear":
        command = clear_display
    elif text == "Back":
        command = backspace
    elif text == "Fact":
        command = calculate_factorial
    elif text == "√":
        command = calculate_root
    else:
        command = lambda t=text: button_click(t)
    
    tk.Button(root, text=text, font=("Arial", 15), width=5, height=2, command=command).grid(row=row, column=col)

# Run the application
root.mainloop()