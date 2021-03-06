import json


# 自定义类
from DjanggoTest import testdb
from hello.models import Test

class MyClass:
    # 初始化
    def __init__(self):
        self.a = 2
        self.b = 'bb'

if __name__ == '__main__':
    # 创建MyClass对象
    myClass = MyClass()
    # 添加数据c
    myClass.c = 123
    myClass.a = 3
    # 对象转化为字典
    myClassDict = myClass.__dict__
    # 打印字典
    print(myClassDict)
    # 字典转化为json
    myClassJson = json.dumps(myClassDict)
    # 打印json数据
    print(myClassJson)
    ##########################
    # json转化为字典
    myClassReBuild = json.loads(myClassJson)
    # 打印重建的字典
    print(myClassReBuild)
    # 新建一个新的MyClass对象
    myClass2 = MyClass()
    # 将字典转化为对象
    myClass2.__dict__ = myClassReBuild;
    # 打印重建的对象
    print(myClass2.a)

    # 将python对象test转换json对象
    test = {"username":"测试","age":16}
    print (type(test))
    print(test["username"])
    python_to_json = json.dumps(test,ensure_ascii=False)
    print (python_to_json)
    print (type(python_to_json))

    # 将json对象转换成python对象
    json_to_python = json.loads(python_to_json)
    print (type(json_to_python))
    print (json_to_python['username'])

    items = ('a', 'b', 'c')
    for item in items:
        entry = Test(name=item)
        entry.save()
    # list = Test.objects.all()
    # print(list)