import time

scale=50
print()

for i in range(1,12):
    if i in(1,6,11):
        print("{0: ^50}".format('-'*20))
    else:
        print("{0: >15}{1: ^20}{2: <15}".format("|","|","|"))
print("正在启动windows...".center(scale,'-'))
print()
for i in range(scale+1):
    a='#'*i
    b='.'*(scale - 1)
    c=(i/scale)*100
    print("\r[{}{}]{:^3.0f}%".format(a,b,c),end='')
    time.sleep(0.3)
print()
print("\n"+"启动完成!".center(scale,'-'))