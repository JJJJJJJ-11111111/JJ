
#如果有500万，左手牵刘昊然，右手搂彭于晏；如果没钱，那就洗洗睡。

# money = 5000000
# if (money >= 5000000):
#     print("左手刘昊然")
#     print("右手彭于晏")
# else:
#     print("那就洗洗睡")

# money = 5000000
#
# if(money < 500000):
#     print("那就洗洗睡")
#
# elif(money <100000 ):
#     print("左手刘昊然")
#
# elif (money < 1000000):
#     print("右手彭于晏")
#
# else:
#     print("右手彭于晏左手刘昊然")

# 循环
# for i in range(50):
#     print("111")

# for i in range (100000000):
#     print(i)
#     print("重要的事情说2遍")

# print(list(range(100))) #起始值，包含边界
# print(list(range(1,10))) #起始值，终止值
# print(list(range(1,10,2))) #起始值，终止值,步长可正可负
# print(list(range(10,0,-1))) #起始值，终止值,步长可正可负
# print(list(range(10,0,-2))) #起始值，终止值,步长可正可负


# while 循环

# i = 1
# while(i<10):
#     print(i)
#     i += 1

# i=1
# while(i):
#     print("bye")

#打印1-10的数据,遇到7不打印
# for i in range (1,11):
#     if(i == 7):
#         pass
#     else:
#       print(i)
#跳过本次循环(continue)
# for i in range (1,11):
#     if(i == 7):
#         continue #跳过continue下方所有代码，进入后面循环
#     else:
#       print(i)

#结束循环 break
# for i in range (1,11):
# #     if(i == 7):
# #         break#跳过continue下方所有代码，进入后面循环
# #     else:
# #       print(i)

#打印出100以内可以被3整除的数
# for i in range(1,100):
#     if (i % 3 == 0):   #判断是否能被3整除用%
#         print(i)
#计算1-100的和
# s = 0
# for i in range(1, 101):
#         s+=i
#         print(s)
#
# 逢七过 （以7结尾或者7的倍数）

# for i in range(1,100):
#    if(i % 7 == 0 or i % 10 == 7 ):
#        print("过")
#    else:
#        print(i)


# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}x{}={}\t'.format(j, i, i * j), end='')
    print()

#冒泡排序

# num7 = 123
#
# print(num7 % 100)  # 余数23
#
# print(num7 % 10)  # 余数3（个位数）
#
# print(int(num7 / 100))  # 1（百位数）
#
# print(int(num7 % 100 / 10))  # 2（十位数）


# for i in range(1,100):
#     print(int(i % 100 / 10 ))