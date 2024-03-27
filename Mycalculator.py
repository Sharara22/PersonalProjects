import tkinter as tk

expression = ""

def add(symbol):
    global expression
    if symbol == "%":  # If the symbol is percentage, add "/100" to the expression
        expression += "/100"
    else:
        expression += str(symbol)  # Otherwise, add the symbol to the expression
    textResult.delete(1.0, "end")  # Clear the textResult widget
    textResult.insert(1.0, expression)  # Insert the updated expression into the textResult widget


def evaluate():
    global expression
    try:
        expression = str(eval(expression))  # Evaluate the expression
        textResult.delete(1.0, "end")  # Clear the textResult widget
        textResult.insert(1.0, expression)  # Insert the result into the textResult widget
    except:
        clear()  # If there's an error, clear the expression
        textResult.insert(1.0, "Error")  # Insert "Error" into the textResult widget

def clear():
    global expression
    expression = ""  # Clear the expression
    textResult.delete(1.0, "end")  # Clear the textResult widget

if __name__ == "__main__":
    gui = tk.Tk()
    gui.configure(background="black")  # Set the background color of the GUI window
    gui.geometry("300x275")  # Set the size of the GUI window
    gui.title("Simple calculator")  # Set the title of the GUI window

    textResult = tk.Text(gui, height=2, width=16, font=("Arial", 24))  # Create a text widget for displaying the result
    textResult.grid(columnspan=5)  # Place the text widget in the GUI window

    gui.resizable(False, False)  # Disable resizing of the GUI window

    # Buttons for numbers
    btn1 = tk.Button(gui, text="1", command=lambda: add(1), width=5, font=("Arial", 14))
    btn1.grid(row=5, column=1)
   
    btn2 = tk.Button(gui, text="2", command=lambda: add(2), width=5, font=("Arial", 14))
    btn2.grid(row=5, column=2)

    btn3 = tk.Button(gui, text="3", command=lambda: add(3), width=5, font=("Arial", 14))
    btn3.grid(row=5, column=3)

    btn4 = tk.Button(gui, text="4", command=lambda: add(4), width=5, font=("Arial", 14))
    btn4.grid(row=4, column=1)

    btn5 = tk.Button(gui, text="5", command=lambda: add(5), width=5, font=("Arial", 14))
    btn5.grid(row=4, column=2)

    btn6 = tk.Button(gui, text="6", command=lambda: add(6), width=5, font=("Arial", 14))
    btn6.grid(row=4, column=3)

    btn7 = tk.Button(gui, text="7", command=lambda: add(7), width=5, font=("Arial", 14))
    btn7.grid(row=3, column=1)

    btn8 = tk.Button(gui, text="8", command=lambda: add(8), width=5, font=("Arial", 14))
    btn8.grid(row=3, column=2)

    btn9 = tk.Button(gui, text="9", command=lambda: add(9), width=5, font=("Arial", 14))
    btn9.grid(row=3, column=3)

    btn0 = tk.Button(gui, text="0", command=lambda: add(0), width=5, font=("Arial", 14))
    btn0.grid(row=6, column=2)

    # Buttons for symbols
    btnDivide= tk.Button(gui, text="/", command=lambda: add("/"), width=5, font=("Arial", 14))
    btnDivide.grid(row=2, column=4)

    btnMultiply = tk.Button(gui, text="x", command=lambda: add("*"), width=5, font=("Arial", 14))
    btnMultiply.grid(row=3, column=4)

    btnMinus = tk.Button(gui, text="-", command=lambda: add("-"), width=5, font=("Arial", 14))
    btnMinus.grid(row=4, column=4)

    btnAdd = tk.Button(gui, text="+", command=lambda: add("+"), width=5, font=("Arial", 14))
    btnAdd.grid(row=5, column=4)

    btnClear = tk.Button(gui, text="C", command=clear, width=5, font=("Arial", 14))
    btnClear.grid(row=2, column=1)

    btnDelete = tk.Button(gui, text="Del", command=lambda: textResult.delete("end-2c", "end-1c"), width=5, font=("Arial", 14))
    btnDelete.grid(row=2, column=2)

    btnPercentage = tk.Button(gui, text="%", command=lambda: add("%"), width=5, font=("Arial", 14))
    btnPercentage.grid(row=2, column=3)

    btnOpenParenthesis = tk.Button(gui, text="(", command=lambda: add("("), width=5, font=("Arial", 14))

    btnOpenParenthesis.grid(row=6, column=1)

    btnCloseParenthesis = tk.Button(gui, text=")", command=lambda: add(")"), width=5, font=("Arial", 14))
    btnCloseParenthesis.grid(row=6, column=3)

    btnEqual = tk.Button(gui, text="=", command=evaluate, width=5, font=("Arial", 14))
    btnEqual.grid(row=6, column=4)

    gui.mainloop()