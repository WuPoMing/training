# 定義函式
from abc import abstractclassmethod


def multiply(n1, n2):
    print(n1*n2)
    return n1*n2

# 呼叫函式
multiply(3, 4)
multiply(6, 8)

value=multiply(3, 4)+multiply(10, 5)
print(value)

# 程式的包裝
def calculate(max):
    sum=0
    for n in range(max+1):
        sum+=n
    print(sum)
calculate(55)