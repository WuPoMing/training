def toFahrenheit(tempC):
    return 9/5*tempC + 32

def toCelsius(tempF):
    return (tempF-32)/9*5

print("__name__:", __name__, end="\n\n")

#將主流程定義在main()函式中
def main():
    tc = float(input("請輸入攝氏溫度:"))
    tf = toFahrenheit(tc)
    print("攝氏%.2f度等於華氏%.2f度" %(tc,tf))
    
#直接執行時呼叫main()函式
if __name__=='__main__':
    main()
