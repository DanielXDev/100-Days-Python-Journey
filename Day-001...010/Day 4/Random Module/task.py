import random
from random import randint
import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)
# print(my_module.my_fav)
#
# random_float = random.random() * 10
# print(random_float)

part = None
deter = random.randint(1, 2)
if deter == 1:
    part = "Head"
else:
    part = "Tail"
print(part)
    