cels = [0,10,20,30,40,50,60,70,80,90,100]

fahs = list(map(lambda x:9/5*x+32, cels))

for c, f in zip(cels, fahs):
    print('攝氏%3d度等於華氏%6.2f度'%(c,f))
