# getting all the numbers that are composed of 1 ,2,3, 4 and the number of digits si different from each other
def GetNumbersBy1234():
    res = []
    m=0
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                    if (i!= j) and (j!=k) and (i!= k):
                        res.append( i + j * 10 + k *100)
                        print (res[m])
                        # print(m)
                        m = m+1


#getting the total bonus which computed by profit user input
def GetBonusByProfit():
    i =int(input('please input profit:'))
    bonus = 0
    print(i)    
    if i<= 10:
        bonus = i*0.1
        print(bonus)
    elif i>10 and i<=20:
        bonus = 1 + (i-10)*0.075
    elif i>20 and i<=40:
        bonus = (i - 20) * 0.05
    elif i>40 and i<=60:
        bonus = (i-40) * 0.03
    elif i>60 and i<=100:
        bonus = (i-60) *0.015
    else:
        bonus = (i-100) * 0.01
    print(bonus)


# 用户输入数字
def Sum(num1 ,num2):
    num1 = input('输入第一个数字：')
    num2 = input('输入第二个数字：')
    
    # 求和
    sum = float(num1) + float(num2)
    
    # 显示计算结果
    print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))
    return sum