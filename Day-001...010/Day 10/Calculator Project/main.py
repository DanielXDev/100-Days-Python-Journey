from idlelib.editor import keynames
from traceback import print_last
import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculate = {
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
new_op = True
while new_op:
    print(art.logo)
    f_num = float(input("What is the first number \n"))
    old_op = True
    while old_op:
        operation = input("Pick a maths operation to carry out \n + \n - \n * \n / \n")
        s_num = float(input("what is the second number \n"))
        result = 0
        for key in calculate:
            if operation == key:
                result = calculate[key](f_num, s_num)
                print(f"{f_num} {key} {s_num} = {result}")
        f_num = result
        ask_user = input(f"Do you want to continue calculating with the old result {result} or start a new operation? yes/no").lower()
        if ask_user  == "no":
            old_op = False
            print("\n" * 15)
            new_op = True