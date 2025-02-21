from tkinter import *
from  tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = [choice(letters) for char in range(randint(8, 10))]
password_list +=[choice(symbols) for sym in range(randint(2, 4))]
password_list +=[choice(numbers) for num in range(randint(2, 4))]

shuffle(password_list)
passwordd = "".join(password_list)

def generate():
    password_entry.insert(0, passwordd)
    pyperclip.copy(passwordd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_dict = {
        website: {
            "Email": username,
            "Password": password
        }
    }

    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Missing Info", message="Please make sure you fill all info")
    else:
        try:
            with open("info.json", "r") as info:
                data = json.load(info)
                data.update(new_dict)
        except FileNotFoundError:
            with open("info.json", "w") as info:
                json.dump(new_dict, info, indent=4)
        else:
            with open("info.json", "w") as info:
                json.dump(data, info, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH FOR WEBSITE LOGS ----------------------#
def search_eng ():
    try:
        with open("info.json", "r") as info_file:
            info = json.load(info_file)
            try:
                web = info[website_entry.get()]
            except KeyError:
                messagebox.askretrycancel(message="Sorry, you don't have any saved info for this site.")
            else:
                messagebox.showinfo(title="Logs", message=f"Email: {web['Email']} \n Password: {web['Password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="You don't have any passwords saved!!")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# window.minsize(width=400, height=400)
window.config(pady=50, padx=50)
window.title("Password Manager")




# -------- Row 0 -------- #
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row= 0, column=1)

# -------- Row 1 -------- #
website_label = Label(text="Website:", font=("Arial", 12, "normal"))
website_label.grid(row=1, column=0)


website_entry = Entry(width=30)
website_entry.focus()
website_entry.grid(row=1, column=1)

website_search_btn = Button(text="Search", font=("Arial", 8, "normal"), command=search_eng, width=17)
website_search_btn.grid(row=1, column=2)

# -------- Row 2 -------- #
username_label = Label(text="Email/Username:", font=("Arial", 12, "normal"), pady=5)
username_label.grid(row=2, column=0)

username_entry = Entry(width=48)
username_entry.insert(0, "daniel@gmail.com")
username_entry.grid(row=2, column=1, columnspan= 2)

# -------- Row 3 -------- #
password_label = Label(text="Password:", font=("Arial", 12, "normal"))
password_label.grid(row=3, column=0)

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

generate_btn = Button(text="Generate Password", font=("Arial", 8, "normal"), command=generate)
generate_btn.grid(row=3, column=2)

# -------- Row 4 -------- #
add_btn = Button(text="Add", width=38, font=("Arial", 9, "normal"), command=save_info)
add_btn.grid(row=4, column=1, columnspan=2, pady=10)















window.mainloop()
