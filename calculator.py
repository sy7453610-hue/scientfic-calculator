import tkinter as tk
import math

# Function to evaluate expression
def click(event):
    global expression
    text = event.widget.cget("text")

    if text == "=":
        try:
            # Replace math functions
            result = str(eval(expression))
            screen_var.set(result)
            expression = result
        except:
            screen_var.set("Error")
            expression = ""

    elif text == "C":
        expression = ""
        screen_var.set("")

    elif text == "sin":
        expression = str(math.sin(float(expression)))
        screen_var.set(expression)

    elif text == "cos":
        expression = str(math.cos(float(expression)))
        screen_var.set(expression)

    elif text == "tan":
        expression = str(math.tan(float(expression)))
        screen_var.set(expression)

    elif text == "log":
        expression = str(math.log10(float(expression)))
        screen_var.set(expression)

    elif text == "√":
        expression = str(math.sqrt(float(expression)))
        screen_var.set(expression)

    elif text == "π":
        expression += str(math.pi)
        screen_var.set(expression)

    elif text == "e":
        expression += str(math.e)
        screen_var.set(expression)

    else:
        expression += text
        screen_var.set(expression)


# Main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x500")

expression = ""
screen_var = tk.StringVar()

# Display screen
screen = tk.Entry(root, textvar=screen_var, font="Arial 20")
screen.pack(fill="both", ipadx=8, pady=10, padx=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["sin", "cos", "tan", "log"],
    ["√", "π", "e", "C"]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 14")
        b.pack(side="left", expand=True, fill="both")
        b.bind("<Button-1>", click)

# Run app
root.mainloop()