# 除法运算
#除数
# a = 10
# b = 20  # 被除数
# if b == 0:
#     print("被除数不能为0")
# else:
#     print( a / b )

#函数（方法）
# def 关键词； div：方法名；a，b  接收外界参数，参数变量必须写在括号（）{括号+参数也叫参数列表}里；表示下方包含一个代码块（方法体）
# def div(a,b):
#     if b == 0:
#         print("不能为0")
#     else:
#         print(a/b)


# def div(a,b):
# #     if b == 0:
# #         print("不能为0")
# #     else:
# #          print(a/b)
# # div(20,30)

#return 表示一个方法的结束，方法返回数据的关键字
#方法的定义
# def select_data(sql):
#       res = "查询结果"
#       return res
#
# result = select_data("")  #方法的调用使用变量接收方法返回值
# print(result)


# def 方法名（变量）:


#参数定义

#位置参数
# def s(a,b):
#     return a+b
# print(s(1,2))

#关键字参数、给参数设置默认值
# 如果调用时没有穿参则用默认值
#关键字、位置同时存在，位置参数在前，关键字参数在后边
# def s(a=1,b=20):
#     return a+b
# print(s(10,20))
#
# #调用传参
#
# #按照位置传参
# print(s(1,2))
# #按照关键字传参
# print(s(b=20))
#
#
# #动态参数定义 #
#
# def ar(*args,a,**kwargs):
#     print(args)       # *arges位置参数传到元祖
#     print(kwargs)     #**kwargs 关键字参数传到字典
#
# ar(1,2,3,4,5,a=10,b=20)



#
# #内置函数
# a = 1000
# print(id(a)) #获取变量内存地址
#
# i = input("sasas") #获取控制台输入
# print(i)
#
# print(type(a)) #获取变量类型
# print(type("sdf"))
#
# print(isinstance("",int)) #判断变量类型
# 1 = [1,2,3,4,5]
# print(len(a)) #获取变量值的个数 支持 list 、tuple、set、dict、str

#操作文件

#九九乘法表
# for i in range(1,10):
#     for j in range (1,i+1):
#         print(j,"X",i,"=",i*j,end="\t")
#     print()


#变量作用域   可以修改变量作用域  （def  class lambda)
#变量搜索规则  就近原则
#局部变量，无法在外部使用
#global可以在局部作用域中声明变量为全局变量
# c = 10 #全局变量
#
# def aaa():
#     global c  #局部变量
#     c = 20
#
# aaa()
# print(c)
#
#
# #字符串
# a = "1234567890"
# b = "456"
#
# print(a+b)  #拼接
# print(a*3)  #复制
# print(a[0])  #根据下标获取单个字符
# print(a[2:6]) #截取3-6的字符
# print(a[:6]) #截取1-6的字符
# print(a[4:])#截取5-0的字符
# print(a[-2:]) #倒着数
# print(a[1:-2]) #截取第二位数到最后第二位数


# a = " sadkddad " #字符串对象
# a = a.strip()
# print(a.strip()) #去除前后空格
# print(a.lstrip()) #去左空格
# print(a.rsplit()) #去右空格
# line = "aa,bb,cc,dd,ee"
# line = line.replace("，",',')  #替换
# print(line)
# print(line.split(','))   #切片
# print(line.find('dd'))

# for i in range(1,10):
#     for j in range (1,i+1):
#         print("{} X {} = {}".format(j,i,i*j),end="\t")
#     print()


#遍历列表
# l = [1,2,3,4,5,6,7,8]
#
# l[ 0 ]=20  #根据下标修改列表元素的值
# l.append(9) # 往列表里末尾添加数据
# l.insert(2,30) #根据下标往列表中插入数据
# l.extend(1,2,3,4,5) #往列表末尾添加多个数据
# l.pop() #删除列表末尾最后一个元素
# l.remove(2) #根据内容删除列表中的数据，有重复只会删除第一个
# print(l.index(6)) #查询某个元素的下标，多个zh

# #元祖
#  t= (1) #一个元素的元祖
#  print(t)
#  #遍历，拼接，截取和字符串列表一致
#  #不支持修改，所以不支持其他操作
#
#  #集合
#  # 空集合
#  s = set()
#  #遍历
#  #不支持下标索引，所以不支持其他操作
#
#
# #字典
# d = {'name':'小明','age':'18','sex':'男'}
#
# print(d["name"])#访问字典值
# d['name'] = '小红' #修改value

545645454564ashjh

亚新无敌

