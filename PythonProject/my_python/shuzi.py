import random

guess=0
tims=1
secret =random.randint(0,100)

print("==========开始游戏==========")
while guess!=secret :
    guess =int(input("数字区间0-100.输入你猜的数字:"))
    print("你输入的数字是",guess)
    if guess==secret:
        print("你猜了{}次，猜对了".format(tims))
    else:
        if guess<secret:
            print("你猜的数字小了")
        else:
            print("你猜的数字大了")
    tims+=1
print("游戏结束")