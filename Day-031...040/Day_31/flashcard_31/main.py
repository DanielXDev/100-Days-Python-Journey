from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FLIP_DELAY = 5000
guessed_words = []
guessed_word = {}


# --------- Creating a word list --------#
try:
    data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    print("Error: CSV file not found!")
    exit()
data_list = [{"French": row.French, "English": row.English} for (index, row) in data.iterrows()]

# --------- Creating the UI ---------- #
window = Tk()
window.title("Flashcard")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)


#---ROW0---#
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_front = PhotoImage(file="images/card_front.png")
image_back = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=image_front)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 290, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# ----------- Display words to the user ----------#
def flip_card(current_word):
    canvas.itemconfig(canvas_img, image=image_back)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=current_word["English"])

def display_words():
    global  guessed_word
    if not data_list:
        canvas.itemconfig(title, text="Well done!")
        canvas.itemconfig(word, text="Completed.")
        return
    else:
        current_word = random.choice(data_list)
        guessed_word = current_word
        canvas.itemconfig(canvas_img, image=image_front)
        canvas.itemconfig(title, text="French")
        canvas.itemconfig(word, text=current_word["French"])
        window.after(FLIP_DELAY, flip_card, current_word)
display_words()


# ----- Tracking and saving progress according to user response ----- #
def correct_ans():
    global data_list
    guessed_words.append(guessed_word)
    data_list = [item for item in data_list if item["French"] != guessed_word["French"]]
    print(len(data_list))
    display_words()




#---ROW1---#
cancel_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

cancel_btn = Button(image= cancel_img, highlightthickness=0, command=display_words)
cancel_btn.grid(row=1, column=0)

right_btn = Button(image=right_img, highlightthickness=0, command=correct_ans)
right_btn.grid(row=1, column=1)














window.mainloop()
