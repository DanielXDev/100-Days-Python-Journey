import turtle
import pandas
class Show:
    def __init__(self):
        self.score = 0
        self.found_states = []
        self.data = pandas.read_csv("50_states.csv")
        self.states = self.data["state"].to_list()
        self.run_game()

    def run_game(self):
        while self.score < 50:
            # Show current score and prompt for an answer
            answer = turtle.textinput(
                title=f"{self.score}/50 Correct States",
                prompt="What's another state's name? (Type 'exit' to quit)"
            )
            # Handle exit command
            if answer is None or answer.lower() == "exit":
                self.save_missing_states()
                break

            self.check_ans(answer)


    def check_ans(self, answer):
        print(self.found_states)
        # answer = turtle.textinput(title=f"{self.score}/50 Correct State", prompt="What's another state's name?")
        for state in self.states:
            if answer.lower() not in self.found_states and answer.lower() == state.lower():
                self.score += 1
                found_state = self.data[self.data.state == state]
                self.found_states.append(found_state.state.values[0].lower())
                self.show_state(found_state)




    def show_state(self, state):
        n = self.score
        write = turtle.Turtle()
        write.penup()
        write.hideturtle()
        x = state.x.values[0]
        y = state.y.values[0]
        write.goto(x, y)
        write.write(f"{state.state.values[0]}", align="center", font=("Ariel", 8, "normal"))

    def save_missing_states(self):
        missing_states = [sta for sta in self.states if sta.lower() not in self.found_states]
        new_data = pandas.DataFrame(missing_states, columns=["state"])
        new_data.to_csv("states_to_learn.csv")
        turtle.exitonclick()
