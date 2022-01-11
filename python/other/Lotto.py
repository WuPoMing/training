import os
import random

os.system("clear")

lotto = random.sample(range(1, 50), 6)
SpecialNumber = random.randint(1, 49)
while SpecialNumber in lotto:
    SpecialNumber = random.randint(1, 49)

# 把 list 中的 int 逐一印出來 
print("中獎號碼:", end=" ")
for l in lotto:
    print(l, end=" ")
print()
print("特別號  :", SpecialNumber)