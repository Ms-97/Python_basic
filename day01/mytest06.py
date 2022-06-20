import random


player = input("홀/짝을 입력하시오: ")

rnum = random.randrange(2)

if rnum == 0:
    com = "홀"
elif rnum == 1:
    com = "짝"    

print("나: "+player)
print("컴: "+com)

if player == com:
    print("결과: 플레이어 승리")
elif player != com:       
    print("결과: 컴퓨터 승리")