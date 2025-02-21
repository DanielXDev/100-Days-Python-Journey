from tkinter import *

window = Tk()
window.title("My First GUI page")
window.minsize(height=400, width=600)

# Label
my_label = Label(text="GUI page label", font=("Ariel", 24, "italic"))
my_label.grid(row= 0, column= 0)


# Entry
my_input = Entry()
my_input.grid(row= 1, column= 1)

# Button
def button_click():
    my_label.config(text=f"{my_input.get()}")

my_button = Button(text="Click me", command=button_click)
my_button.grid(row= 0, column= 2)


# Button2

def button2_click():
    print("Me")

my2_button = Button(text="Click Me", command= button2_click)
my2_button.grid(row= 2, column= 3)













window.mainloop()