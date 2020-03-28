import os
# 打开
file_read = open("learn_file")
file_write = open("learn_file[副本]", "w")

# 读写
text = file_read.read()
file_write.write(text)

# 关闭
file_read.close()
file_write.close()
