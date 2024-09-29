from tkinter import *

# Creating window

window = Tk()
window.title("Miles to Kilometer converter")
window.config(padx=100, pady=30)
window.minsize(width=300, height=200)


# Functions

def button_clicked():
    value = input.get()
    resultLabel["text"] = (round(float(value)/1.609344, 2))



# Widgets

# Reference Label
empty = Label(text="")
empty.grid(column=0, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=1)

label1 = Label(text="is equal to")
label1.grid(column=0, row=2)

resultLabel = Label(text="0")
resultLabel.grid(column=1, row=2)

label2 = Label(text="Kilometers")
label2.grid(column=2, row=2)

# Entry

input = Entry(width=10)
input.grid(column=1, row=1)

# Button
calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=3)


window.mainloop()
