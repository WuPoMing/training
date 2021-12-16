import os
os.system("clear")
'''
# 定義裝飾器
def myDeco(cb):
    def run():
        print("裝飾器中的程式碼")
        cb(5)
    return run

# 使用裝飾器
@myDeco
def test(n):
    print("普通函式的程式碼", n)

test()
'''
# 定義一個裝飾器計算 1+2+3+...+50 的總和
def calculate(cb):
    def run():
        # 裝飾器想要執行的程式碼
        result = 0
        for n in range(51):
            result += n
        # 把計算結果透過參數傳到被裝飾的函式中
        cb(result)
    return run

# 使用裝飾器
@calculate
def show(n):
    print("計算結果是", n)

@calculate
def showEnglish(n):
    print("Result is", n)

show()
showEnglish()