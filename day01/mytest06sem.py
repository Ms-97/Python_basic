import random

com = ""
mine = ""
result = ""

mine = input("홀/짝을 고르시오")

rnd = random.random()

if rnd > 0.5:
    com = "홀"
else:
    com = "짝"

if com == mine:
    result = "이김"
else:
    result = "짐"

print("mine",mine)
print("com",com)
print("result",result)