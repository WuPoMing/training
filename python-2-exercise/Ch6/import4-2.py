import temperature2 as temp

#匯入模組時不呼叫main()函式
tf = float(input("請輸入華氏溫度:"))
tc = temp.toCelsius(tf)

print("華氏%.2f度攝氏等於%.2f度" %(tf,tc))
