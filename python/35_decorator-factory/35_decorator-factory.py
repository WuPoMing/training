import os
os.system("clear")
'''
def myFactory(base):
    def myDeco(cb):
        def run():
            print("裝飾器內的程式", base)
            result = base*2
            cb(result)
        return run
    return myDeco

@myFactory(5)
def test(result):
    print("普通函式的程式", result)

test()
'''
# 計算 1+2+3+...+50 的裝飾器
def calculateFactory(max):    
    def calculate(cb):
        def run():
            total = 0
            for n in range(max):
                total += n
            cb(total)
        return run
    return calculate

@calculateFactory(100)
def show(result):
    print("結果是", result)

@calculateFactory(10)
def showEnglish(result):
    print("Result is", result)

show()
showEnglish()