def toFahrenheit(tempC):
    return 9/5*tempC + 32

def toCelsius(tempF):
    return (tempF-32)/9*5

print("__name__:", __name__, end="\n\n")

tc = float(input("請輸入攝氏溫度:"))
tf = toFahrenheit(tc)
print("攝氏%.2f度等於華氏%.2f度" %(tc,tf))
