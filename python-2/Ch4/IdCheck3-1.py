places = {'A':'臺北市', 'B':'臺中市', 'C':'基隆市', 'D':'臺南市', 'E':'高雄市', 'F':'新北市',
          'G':'宜蘭縣', 'H':'桃園市', 'I':'嘉義市', 'J':'新竹縣', 'K':'苗栗縣',
          'M':'南投縣', 'N':'彰化縣', 'O':'新竹市', 'P':'雲林縣', 'Q':'嘉義縣', 'T':'屏東縣',
          'U':'花蓮縣', 'V':'臺東縣', 'W':'金門縣', 'X':'澎湖縣', 'Z':'連江縣',
          'L':'臺中縣', 'R':'臺南縣', 'S':'高雄縣', 'Y':'陽明山'}
pNum = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':34, 'J':18, 'K':19,
        'M':21, 'N':22, 'O':35, 'P':23, 'Q':24, 'T':27, 'U':28, 'V':29, 'W':32, 'X':30, 'Z':33,
        'L':20, 'R':25, 'S':26, 'Y':31}

weight = [8,7,6,5,4,3,2,1,1]

# A123456789

def isValidId(pid):
    if(pid[0] not in pNum):
        #print(pid[0])
        return False
    if(pid[1]!='1' and pid[1]!='2'):
        #print(pid[1])
        return False
    checkSum = 0
    checkSum = p2sum(pNum[pid[0]])
    for i in range(1, 10):
        #print("%d:%s" %(i,pid[i]))
        checkSum += int(pid[i])*weight[i-1]
    #print(checkSum)
    if(checkSum%10==0):  
        return True
    else:            
        return False  

def p2sum(num):
    return num//10*1+num%10*9

pid = input('輸入身分證字號:')

if(isValidId(pid)):
    gender = int(pid[1])
    birth = pid[0]
    if(gender == 1):
        print('先生您好!')
    else:
        print('小姐您好!')
    print('出生地:', places[birth])
else:
    print('身份證字號無效:%s' %pid)
