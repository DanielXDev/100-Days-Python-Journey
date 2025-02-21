from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    per_question = Question(question["text"], question["answer"])
    question_bank.append({"text": per_question.text, "answer": per_question.ans})

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print(f"You've completed the quiz. Your final score is {quiz.score}/{len(question_bank)}")
