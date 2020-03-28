import random
def GuessSecret(maxtimes):
    print("==========开始游戏==========")

    tims=1
    print("你有{}次机会！".format(maxtimes))

    for i in range(maxtimes):
        guess = int(input("数字区间0-100.输入你猜的数字:"))
        if guess == secret:
            print("你猜了{}次，猜对了".format(tims))
            print("游戏结束")
            break
        else:
            if guess < secret:
                print("你猜的数字小了")
            else:
                print("你猜的数字大了")
            print("你还可以猜{}次".format(maxtimes - tims))
        tims += 1
        if i == maxtimes-1:
            print("很遗憾你没有次数了哦！")

    exit(0)

guess = 0
global tims
secret = random.randint(0, 100)

maxtimes = int(input("输入你猜的最大次数:"))

GuessSecret(maxtimes)



