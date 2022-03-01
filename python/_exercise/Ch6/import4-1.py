import temperature1 as temp

tf = float(input("請輸入華氏溫度:"))
tc = temp.toCelsius(tf)

print("華氏%.2f度攝氏等於%.2f度" %(tf,tc))
