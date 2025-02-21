import requests


response = requests.get(url="https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean")
response.raise_for_status()

data = response.json()
result_list = data["results"]
question_data = [{"question": key["question"], "correct_answer": key["correct_answer"], "incorrect_answers": key["incorrect_answers"]} for key  in result_list]

# print(data["results"])
# print(question_data)
