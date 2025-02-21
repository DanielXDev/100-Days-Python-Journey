
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
after_count = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global rep
    rep = 0
    window.after_cancel(id=after_count)
    page_label.config(text="Timer")
    check_mark.config(text="")
    canvas.itemconfig(img_text, text= "00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep
    rep += 1
    # seconds = 0
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if rep % 2 == 0 and rep != 8:
        page_label.config(text="Break")
        seconds = short_break_secs
    elif rep == 8:
        page_label.config(text="Break")
        seconds = long_break_secs
        rep = 0
    else:
        page_label.config(text="Work")
        seconds = work_secs
    count_down(seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global after_count
    mins = int(count / 60)
    minutes = mins if mins > 10 else f"{0}{mins}"
    secs = count % 60
    seconds = secs if secs > 9 else f"{0}{secs}"
    canvas.itemconfig(img_text, text=f"{minutes}:{seconds}")
    if count > 0:
        after_count = window.after(1000, count_down, count - 1)
    elif count == 0:
        global rep
        checks = ["✔", "✔✔", "✔✔✔", "✔✔✔✔"]
        if rep % 2 == 0:
            check_mark.config(text=f"{checks[int(rep/2) -1]}")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(height=400, width=400)
window.config(padx=70, pady=70, bg=YELLOW)

page_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
page_label.grid(row=0, column=1)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
img_text = canvas.create_text(102, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start_btn = Button(text="Start", font=(FONT_NAME, 12, "bold"), command=start_timer)
start_btn.grid(row=2, column=0)

check_mark = Label( bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, "bold"))
check_mark.grid(row=3, column=1)

restart_btn = Button(text="Restart", font=(FONT_NAME, 12, "bold"), command= reset_timer)
restart_btn.grid(row=2, column=2)




window.mainloop()

