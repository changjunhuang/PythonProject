# 分行读
file = open("learn_file")

while True:
    text = file.readline()

    # 文件不存在
    if not text:
        break
    print(text)

file.close()