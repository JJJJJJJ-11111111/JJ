# # 1、编写一个返回随机手机号的方法
#
# '''
# 用一个列表，存储所有的有效号段字符串
# 随机生成一个长度8位的数字字符串
#
# '''
# import random
#
#
# def phone():
#     hao_duan_list = ["131",'185','181','183','182','184','186','187','188','189',"131","130","132","133","134","135","136"]
#     hao_duan = random.choice(hao_duan_list)
#     res = random.choices("0123456789",k=8)
#     ba_wei = "".join(res)
#     return hao_duan + ba_wei
#
# print(phone())
#
#
# # 2、编写一个返回指定长度和内容的随机字符串方法
# def random_str(str, length):
#     res = random.choices(str, k=length)
#     return "".join(res)
#
#
# print(random_str("abcdefghijklmnopqrstuvwxyz1234568790",10))
#
# # 3、编写一个返回随机姓名的方法
#
# '''
# 姓
# 名字 1 - 2
#
# 姓列表
# 名字 字的取值范围列表
# 随机获取1-2的随机整数
# 获取名字的字
#
#
# '''
# def random_name():
#     xing_list = ["赵","钱","孙","李","周","武","郑","王","欧阳","诸葛","轩辕","上官","司徒"]
#     zi_list = "花赤橙黄绿青蓝紫冬梅建国华世凯"
#     xing = random.choice(xing_list)
#     zi_length = random.randint(1,2)
#     zi = random_str(zi_list,zi_length)
#     return xing + zi
#
# print(random_name())




#try except 抓异常  except 可以指定捕获异常的类型 exception表示任意异常类型

# try:
#     r = open("a.txt",'r')
#     print(1 / 1)
# except ZeroDivisionError as e :#后面可加捕获异常的类型
#     print(e)
#     print("程序执行遇到了问题")
#     print("重新打卡")
# else:
#     print("程序运行没有报错")
# finally:
#     print("不管程序有没有报错都会运行")
#
# print("文件已经打卡")


'''
代码多人协同
svn
git
1、本机电脑
安装git软件

2、远程代码仓库
github

本地仓库创建
git


gitee  阿里巴巴
gitlab  腾讯


'''