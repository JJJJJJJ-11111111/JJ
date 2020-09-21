# #面对对象编程
# def s(a,b):
#     return a + b
# print(s(10,20))
#
# #对变量和方法的打包
#
#
#  #类和对象
#  #创建类
# class str_demo():   #创建
#
#      s = None #属性 类加载到内存中就会被创建  类变量和方法平级  程序运行结束类才销毁
#
#     def replace(self):  #类里面的变量自带self 代表类本身 对象被销毁时同步销毁
#         self.a ="实例变量" #实例变量,方法运行结束就被销毁
#         b = "局部变量"
#         print("字符串替换")
#
#
#
#     def splist(self):  # 类里面的变量自带self 代表类本身
#         print("字符串切割")
#
#
#
# #实例化
# sd = str_demo()  #创建实例化  sd 就是一个对象
# sd.s = "hello"
# sd.replace()
# sd.split()
# #类外部访问
# #类变量
# print(str_demo.s)  #通过类名直接访问（推荐）
# #实例变量
# sd = str_demo() #实例化一个对象
# sd.replace() #调用实例方法创建 实例变量
# print(sd.a) #通过对象访问实例变量
# print(sd.s)  #可通过对象访问类变量（不推荐）
# sd.s ="s是一个实例变量" #创建一个实例变量
# print(sd.s) #访问实例变量s
# print(str_demo.s) #访问类变量s
#
# class str_demo():
#
#     # 不需要显式调用，程序自动调用的
#     def __init__(self):
#         print("魔法方法")
#
#     # 实例方法
#     def replace(self):
#         print("实例方法")
#         pass
#
#     @classmethod # 装饰器
#     def split(cls):
#         print("类方法")
#
#     @staticmethod
#     def static():
#         print("静态方法")


#
# class str_demo():
#
#     # 不需要显式调用，程序自动调用的
#     def __init__(self):
#         print("魔法方法")
#
#     # 实例方法
#     def replace(self):
#         print("实例方法")
#         pass
#
#     @classmethod # 装饰器
#     def split(cls):
#         print("类方法")
#
#     @staticmethod
#     def static():
#         print("静态方法")
#
#
#
# # 类外部调用方法
# str_demo.split() # 调用类方法
# str_demo().replace() # 通过对象调用实例方法
# str_demo.static() # 通过类名调用静态方法
# str_demo().static() # 通过对象调用静态方法
# str_demo() # 调用__init__魔法方法
#
#
# class str_demo():
#     b = "类变量"
#     # 不需要显式调用，程序自动调用的
#     def __init__(self):
#         self.a="实例变量"
#         print("魔法方法")
#         self.replace() # 在实例方法中调用实例方法
#         __class__.split() # 在实例方法中调用类方法
#         __class__.static()  # 在实例方法中调用静态方法
#         self.static()  # 在实例方法中调用静态方法
#
#
#     # 实例方法
#     def replace(self): # self代表当前对象本身
#         print("实例方法")
#
#
#     @classmethod
#     def class_method(cls):# cls 代表当前类本身
#         # 不能调用实例方法
#         cls.split() # 调用类方法
#         cls.static()# 调用静态方法
#
#
#     @classmethod # 装饰器
#     def split(cls):
#         print("类方法")
#
#     @staticmethod
#     def static_method():
#         # 不能调用实例方法
#         __class__.split()  # 调用类方法
#         __class__.static()  # 调用静态方法
#     @staticmethod
#     def static():
#         print("静态方法")



# 类外部调用方法
# str_demo.split() # 调用类方法
# str_demo().replace() # 通过对象调用实例方法
# str_demo.static() # 通过类名调用静态方法
# str_demo().static() # 通过对象调用静态方法
# str_demo() # 调用__init__魔法方法

# 在类内部调用方法
# str_demo()# 实例方法
# str_demo.class_method()# 类方法
# str_demo.static_method() # 静态方法

#类的封装 私有加__ ,公开无



#类的继承
# class Parent():
#
#     first_name='王'
#     second_name = '五'
#
#     def ji_neng(self):
#         print("锁匠")
#
# class Son(parent):
#     pass
#
# son - =



# 多态-子类中，对父类的重写
# class Parent():
#
#     def ji_neng(self):
#         print("开锁")
#
# class Son(Parent):
#
#     def ji_neng(self):
#         super().ji_neng()
#         print("盗窃")
#
# p = Parent()
# p.ji_neng()
# s = Son()
# s.ji_neng()



#from.....import ..  跨模块引用

# import os #路径操作
#
# print(os.listdir( '.' ))#获取指定文件夹下所有文件
# print(os.path.exists("a.txt"))#判断文件或文件夹是否存在
# print(os.path.abspath("a.txt"))  #获取文件的路径（不会判断文件是否存在）
# print(os.path.join("E:\\softdwareata\\python\\base_2008A\\","a.txt")) #拼接文件路径
# os.system("dir") #执行cmd 命令


#随机模块
# import random
# print(random.randint(1,20)) #获取随机整数
# print(random.random()) #获取随机数 小数
# print(random.choice("0123456789")) #在指定集合中随机获取一个数据
# print(random.choices("0123456789",k= 10)) #在指定集合中，随机获取一组数据
# print("，".join(random.choices("0123456789",k= 10)))   #把可迭代对象转成字符串
#
#
# import re
# a = "我叫：AA,我今年18岁"
# r = re.compile("岁(.*?)岁")

# import time
#
# print(time.time()) #获取秒级时间戳
# t = time.localtime(time.time()) #把时间戳转换为时间结构体
# str_time = time.strftime("%Y-%m-%d %H:%M:%S",t) #把时间结构转行成时间类型的字符串
# print(str_time)
# t = time.strptime(str_time,"%Y-%m-%d %H:%M:%S")
# time_stamp = time.mktime()
# print(time_stamp)


#第三方模块


#requestst


#1、pip 工具下载并安装第三方模块requests
#2、from import  导入刚安装的第三方模块
#3、使用其中的代码
import random

import requests


'''
pip install  第三方模块名  下载并安装第三方模块
pip uninstall 第三方模块名  卸载第三方模块
pip  list   查看所有已安装第三方模块
pip freeze > requirements.txt   导出所有已安装的第三方模块名及版本至文件中
pip freeze >-r  requirements.txt  安装文件中所有的第三方模块


'''
'''
1、编写一个返回随机手机号的方法
2、编写一个返回指定长度和内容的随机字符串方法
3、编写一个返回随机姓名的方法
'''
#1、编写一个返回随机手机号的方法
def zz ():
   import random
   l = random.choices("0123456789",k=8)
   s = str(random.choice(['189','177','136','151','150','135','132']))
   return print(s+"".join(l))
zz()

#2、编写一个返回指定长度和内容的随机字符串方法
def xx ():
    import random
    i= random.choices("jhdjdjdjdjwdj545454",k=5)
    return print("".join(i))
xx()
#3、编写一个返回随机姓名的方法
def cc ():
    import  random












