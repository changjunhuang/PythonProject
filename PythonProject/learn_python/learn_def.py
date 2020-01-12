def learn_def(num1, num2):
    """
    这是一个python的函数
    """
    print("hello python")
    print("hello def")
    result = int(num1) + int(num2)
    return result


def demo(*temp, **dis ):
    print(temp)
    print(dis)


# 数组 元素同类型 类似list
list = ["huang", "chang", "jun", "kao", "qing", "hua"]
# 元组 元素不同类型
tuple_list = ("小明", 21, 18.75)
# 字典 kv存储，k类型相同，类似map
dis = {"name": "小明",
       "age": 18,
       "length": 18.75}
# 字符串
str = "huang chang jun kao qing hua"


class python:
    # 这是一个类

    name = "hello python"

    __age = 100

    def __init__(self, name):
        print("初始化方法调用，名字被赋值为：" + name)
        self.name = name

    def __del__(self):
        print("对象被回收")

    def index(self):
        print("index方法被调用")

    def private(self):
        print(self.__age)

    @classmethod
    def clazzMethod(cls):
        print("类方法被调用，这是一个类方法")
        print("类方法调用类属性：" + cls.name)

    # 静态方法
    @staticmethod
    def staticMethod():
        print("静态方法被调用")

    # 异常捕获
    def catchError(self):
        try:
            address = int(input("请输入一个地址："))
            print(address)
        except Exception as address:
            print("输入的不是数字类型 %s" % address)
        finally:
            print("finally代码，无论是否成功都要输出!")


xiaopi = python("huangchangjun")
xiaopi.index()
print(xiaopi.name)
print(python.name)
python.clazzMethod()
python.staticMethod()
xiaopi.catchError()
