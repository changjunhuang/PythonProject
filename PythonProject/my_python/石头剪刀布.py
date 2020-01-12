import random

allList = ["剪刀", "石头", "布"]

winList = [["石头，剪刀"], ["剪刀", "布"], ["布", "石头"]]

chnum = 0
prompt = ''

while True:
    chnum = int(input("输入你的数字："))
    if chnum not in [0, 1, 2, 3]:
        print("无效的选择,请选择0/1/2/3")
        continue
    if chnum == 3:
        break
    cchoice = random.choice(allList)
    uchoice = allList[chnum]
    print("您选择了：{}\n计算机选择了：{}".format(uchoice, cchoice))
    if uchoice == cchoice:
        print("平局")
    elif [uchoice, cchoice] in winList:
        print("你赢了")
    else:
        print("你输了")
print("游戏结束")
