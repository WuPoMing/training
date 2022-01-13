# 有五次機會猜1~100之間的整數
import os
import random

os.system("clear")

lower, upper = 1, 100
answer = random.randint(lower, upper)

for i in range(5):
    guess = int(input(("請猜{}~{}之間的整數 : " .format(lower, upper))))
    while guess > upper or guess < lower:
        print("==========")
        print("輸入錯誤!")
        print("==========")
        print("剩下{}次機會!".format(5-i))
        guess = int(input(("請重新猜{}~{}之間的整數 : " .format(lower, upper))))
    if guess == answer:
        print("猜中了!!!!!!!!!!")
        break
    elif guess > answer:
        upper = guess - 1
    else:
        lower = guess + 1
    if 4-i > 0:
        print("剩下{}次機會!".format(4-i))
    
else:
    print("答案是 : ", answer)
    print("遊戲結束!")