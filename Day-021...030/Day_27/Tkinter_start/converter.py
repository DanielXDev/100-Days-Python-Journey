from tkinter import *

window = Tk()
window.minsize(width=200, height=200)
window.title("Converter")
window.config(padx=50, pady=40)


#First row

user_entry = Entry()
user_entry.grid(column=1, row=0)

row0_label = Label(text="miles", font=("Ariel", 12))
row0_label.grid(column=2, row=0)

#Second row

row1_label1 = Label(text="is equal to", font=("Ariel", 12), pady=20)
row1_label1.grid(column=0, row=1)

row1_label2 = Label(text=f"0", font=("Ariel", 12))
row1_label2.grid(column=1, row=1)


row1_label3 = Label(text="km", font=("Ariel", 12))
row1_label3.grid(column=2, row=1)


#Third row
def calc():
    answer = round(int(user_entry.get()) * 1.609)
    row1_label2.config(text=answer)
calculate_btn = Button(text="Calculate", command=calc)
calculate_btn.grid(column=1, row=2)
calculate_btn.config(width=15)














window.mainloop()