# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext

from hello.models import Test, Contact

# 数据库操作,新增
# from django.db import transaction
# @transaction.commit_manually
def testdb(request):
    items = ('pig1','dog1','cat1')
    for item in items:
        entry = Test(name=item)
        entry.save()
    # transaction.commit()
    return HttpResponse("<p>数据添加成功！</p>")

# 数据库操作，查询
def testdb1(request):
    # 初始化
    response = ""
    response1 = ""
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=5)
    # 获取单个对象
    response3 = Test.objects.get(id=1)
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    response4 = Test.objects.order_by('name')[0:2]
    # 数据排序
    response5 = Test.objects.order_by("id")
    # 上面的方法可以连锁使用
    response6 = Test.objects.filter(name="dog").order_by("id")
    # 输出所有数据
    num = 0
    listStr =[]
    for var in list:
        num += 1
        myClassDict = var.__dict__
        print(myClassDict)

        myClassJson = json.dumps(myClassDict, default=lambda obj: obj.__dict__)
        # 打印json数据
        print(myClassJson)
        response1 += myClassJson + ", "
        listStr.append(myClassJson)
        dic = json.loads(myClassJson)
        print('do=',dic)

    response = response1
    print('fd=',type(list))

    # return HttpResponse("<p>" + response + str(num) + str(len(list)) + "</p>")

    return render_to_response("testdb.html", {"dic": dic,"listStr": list, })
    # return render(request, 'testdb.html', dic)
    # return render(request, 'testdb.html', {'listStr': listStr})
    return  render()

# 数据库操作，更新
def testdb2():
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Test.objects.get(id=4)
    test1.name = 'Google1'
    test1.save()
    # 另外一种方式
    Test.objects.filter(id=3).update(name='sunhao')
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    return HttpResponse("<p>修改成功</p>")

# 数据库操作 删除数据
def testdb3(request):
    # 删除id=1的数据
    # test1 = Test.objects.get(id=2)
    # test1.delete()
    # 另外一种方式
    Test.objects.filter(id=8).delete()
    # 删除所有数据
    # Test.objects.all().delete()
    return HttpResponse("<p>删除成功</p>")

# 数据库Contacts操作，查询
def queryContact(request):
    # 初始化
    response = ""
    response1 = ""
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Contact.objects.all()
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=5)
    # 获取单个对象
    response3 = Test.objects.get(id=1)
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    response4 = Test.objects.order_by('name')[0:2]
    # 数据排序
    response5 = Test.objects.order_by("id")
    # 上面的方法可以连锁使用
    response6 = Test.objects.filter(name="dog").order_by("id")
    # 输出所有数据
    num = 0
    listStr =[]
    for var in list:
        num += 1
        myClassDict = var.__dict__
        print(myClassDict)

        myClassJson = json.dumps(myClassDict, default=lambda obj: obj.__dict__)
        # 打印json数据
        print(myClassJson)
        response1 += myClassJson + ", "
        listStr.append(myClassJson)
        dic = json.loads(myClassJson)
        print('do=',dic)

    response = response1
    print('fd=',type(list))

    # return HttpResponse("<p>" + response + str(num) + str(len(list)) + "</p>")

    return render_to_response("testdb.html", {"dic": dic,"listStr": list, })
    # return render(request, 'testdb.html', dic)
    # return render(request, 'testdb.html', {'listStr': listStr})
    return  render()


