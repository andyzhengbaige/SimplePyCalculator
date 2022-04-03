from re import I
import tkinter as tk
from tkinter import Label, ttk

root = tk.Tk()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

sum = 0
sign = ""
numb = 0
y = 0
deci = 0
i = 0.1
def manipulation(s):
    global sign, deci, i
    sign = s
    deci = 0
    i = 0.1
    label = Label(root, text=s)
    label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5, columnspan = 4, rowspan = 2)

def num(n):
    global numb
    global y
    global i
    if not sign:
        if deci == 0:
            numb *= 10
            numb += int(n)
            label = Label(root, text=numb)
            label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5, columnspan = 4, rowspan = 2)
        else:
            numb += float(n) * i
            i /= 10
            label = Label(root, text=numb)
            label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5, columnspan = 4, rowspan = 2)
    else:
        if deci == 0:
            y *= 10
            y += int(n)
            label = Label(root, text=y)
            label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5, columnspan = 4, rowspan = 2)
        else: 
            y += float(n) * i
            i /= 10
            label = Label(root, text=y)
            label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5, columnspan = 4, rowspan = 2)

def summing():
    global sum
    if sign == '+':
        sum = numb + y
        label = Label(root, text=round(sum,3))
        label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5, columnspan = 4, rowspan = 2)
    elif sign == '-':
        sum = numb - y
        label = Label(root, text=round(sum,3))
        label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5, columnspan = 4, rowspan = 2)
    elif sign == '*':
        sum = numb * y
        label = Label(root, text=round(sum,3))
        label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5, columnspan = 4, rowspan = 2)
    elif sign == '/':
        sum = numb / y
        label = Label(root, text=round(sum,3))
        label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5, columnspan = 4, rowspan = 2)

def clear_var():
    global sum, numb, y, sign, i, deci
    sum = 0
    numb = 0
    y = 0
    sign = 0
    i = 0.1
    deci = 0
    label = Label(root, text=sum)
    label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5, columnspan = 4, rowspan = 2)

def decimals():
    global deci
    deci = 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

window_width = 250
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

centre_x = int(screen_width/2 - window_width/2)
centre_y = int(screen_height/2 - window_height/2)

root.title('Simple Calculator')
title = root.title()
root.geometry(f'{window_width}x{window_height}+{centre_x}+{centre_y}')
root.resizable(False, False)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=2)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)

label = Label(root, text=sum)
label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5, columnspan = 4, rowspan = 2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

adding = ttk.Button(root, text ='+', command = lambda: manipulation('+'))
adding.grid(column=3, row=5, sticky=tk.EW, padx=5, pady=5)


subtracting = ttk.Button(root, text = '-', command = lambda: manipulation('-'))
subtracting.grid(column=3, row=4, sticky=tk.EW, padx=5, pady=5)

multiplying = ttk.Button(root, text = 'x', command = lambda: manipulation('*'))
multiplying.grid(column=3, row=3, sticky=tk.EW, padx=5, pady=5)

dividing = ttk.Button(root, text = '/', command = lambda: manipulation('/'))
dividing.grid(column=3, row=2, sticky=tk.EW, padx=5, pady=5)

one = ttk.Button(root, text ='1', command = lambda: num('1'))
one.grid(column=0, row=5, sticky=tk.EW, padx=5, pady=5)

two = ttk.Button(root, text ='2', command = lambda: num('2'))
two.grid(column=1, row=5, sticky=tk.EW, padx=5, pady=5)

three = ttk.Button(root, text ='3', command = lambda: num('3'))
three.grid(column=2, row=5, sticky=tk.EW, padx=5, pady=5)

four = ttk.Button(root, text ='4', command = lambda: num('4'))
four.grid(column=0, row=4, sticky=tk.EW, padx=5, pady=5)

five = ttk.Button(root, text ='5', command = lambda: num('5'))
five.grid(column=1, row=4, sticky=tk.EW, padx=5, pady=5)

six = ttk.Button(root, text ='6', command = lambda: num('6'))
six.grid(column=2, row=4, sticky=tk.EW, padx=5, pady=5)

seven = ttk.Button(root, text ='7', command = lambda: num('7'))
seven.grid(column=0, row=3, sticky=tk.EW, padx=5, pady=5)

eight = ttk.Button(root, text ='8', command = lambda: num('8'))
eight.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)

nine = ttk.Button(root, text ='9', command = lambda: num('9'))
nine.grid(column=2, row=3, sticky=tk.EW, padx=5, pady=5)

zero = ttk.Button(root, text ='0', command = lambda: num('0'))
zero.grid(column=0, row=6, sticky=tk.EW, padx=5, pady=5, columnspan = 2)

equating = ttk.Button(root, text = '=', command = lambda: summing())
equating.grid(column=3, row=6, sticky=tk.EW, padx=5, pady=5)

clearing = ttk.Button(root, text = 'AC', command = lambda: clear_var())
clearing.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)

decimal = ttk.Button(root, text = '.', command = lambda: decimals())
decimal.grid(column=2, row=6, sticky=tk.EW, padx=5, pady=5)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
root.mainloop()