import os
os.system("clear")

# # 定義生成器函式
# def test():
#     print("階段一")
#     yield 5
#     print("階段二")
#     yield 10

# # 呼叫並回傳生成器
# gen = test()

# # 搭配 for 迴圈使用
# for d in gen:
#     print(d)

def generateEven(maxNumber):
    num = 0
    while num<=maxNumber:
        yield num
        num += 2

evenGenerator = generateEven(10)
for d in evenGenerator:
    print(d)