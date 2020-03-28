# 1.打开文件
file = open("learn_file", "w+")

# 读取文件
text = file.read()
print(text)

# 改写文件
# file.write("//n new context")

# 打印文件
print(text)
# 关闭文件
file.close()
