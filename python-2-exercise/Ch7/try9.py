num1 = 10
num2 = 0
nums = [1,3,5,7,9]
try:    
    #print(num1/num2)
    #print(num1*num3)
    print(nums[100])
except Exception as ex:
    print("例外類別:", type(ex))
    print("例外訊息:", str(ex))
finally:
    print('結束')
