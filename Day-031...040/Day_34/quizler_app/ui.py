from functools import partial
from tkinter import *
import textwrap
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class UserInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        #First row
        self.score_label = Label(text="Score: 0", font=("Arial", 16, "normal"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)


        #Second row
        self.canvas = Canvas(height=300, width=400, bg="white")
        self.question = self.canvas.create_text(200, 150,
                                text="Some text",
                                font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column= 0, columnspan= 2, pady=50)

        #Third row
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.right_btn = Button(image=self.true_img, highlightthickness=0, command=partial(self.check_ans, "True"))
        self.wrong_btn = Button(image=self.false_img, highlightthickness=0, command=partial(self.check_ans, "False"))
        self.right_btn.grid(row=2, column=0)
        self.wrong_btn.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=f"{textwrap.fill(q_text, width=30)}")
        else:
            self.canvas.itemconfig(self.question, text="You've completed the quiz")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")


    def check_ans(self, value):
        is_right = self.quiz.check_answer(value)
        self.give_feedback(is_right)

    def give_feedback(self, ans):
        if ans:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)


