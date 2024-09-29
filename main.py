from tkinter import *

# Creating window

window = Tk()
window.title("Miles to Kilometer converter")
window.config(padx=100, pady=30)
window.minsize(width=300, height=200)


# Functions

def button_clicked():
    value = miles_input.get()
    result_label["text"] = (round(float(value) / 1.609344, 2))


# Widgets

# Reference Label
empty = Label(text="")
empty.grid(column=0, row=0)

miles_Label = Label(text="Miles")
miles_Label.grid(column=2, row=1)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=2)

result_label = Label(text="0")
result_label.grid(column=1, row=2)

kilometers_label = Label(text="Kilometers")
kilometers_label.grid(column=2, row=2)

# Entry

miles_input = Entry(width=10)
miles_input.grid(column=1, row=1)

# Button
calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=3)

window.mainloop()
