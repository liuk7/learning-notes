# a = 321
# b = 123
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)
# print(a < b)

# a = int(input('a = '))
# b = int(input('b = '))
# print('a + b = %d' % (a + b))
# print('a - b = %d' % (a - b))
# print('a * b = %d' % (a * b))

# a = 100
# b = 12.345
# c = 1 + 5j
# d = 'hello, world'
# e = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# flag5 = not flag1
# print("flag1 = ", flag1)
# print("flag2 = ", flag2)
# print("flag3 = ", flag3)
# print("flag4 = ", flag4)
# print("flag5 = ", flag5)
# print(flag1 is True)
# print(flag2 is not False)

# f = float(input('请输入华氏温度： '))
# c = (f - 38) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# c = float(input('请输入摄氏温度：'))
# f = c * 1.8 + 38
# print('%.1f摄氏度 = %.1f华氏度' % (c, f))

# import math

# r = float(input('请输入圆的半径：'))
# a = r ** 2 * math.pi
# p = 2 * math.pi * r
# print('圆的面积为：%.4f, 圆的周长为：%.4f' % (a, p))

# year = int(input('请输入年份：'))
# is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
# print(is_leap)


# while True :    
#     value = float(input('请输入长度：'))
#     unit = input('请输入单位：')
#     if unit == 'inch' or unit == '英寸':
#         print('%.2f英寸=%.2f厘米' % (value, value * 2.54))
#         break
#     elif unit == 'cm' or unit == '厘米':
#         print('%.2f厘米=%.2f英寸' % (value, value / 2.54))
#         break
#     else :
#         print('单位错位，请重新输入')
#         continue

# from random import randint

# face = randint(1, 100)

# if face == 1 :
#     print('小')
# elif face > 1 and face < 100 :
#     print('重新来')
#     print(face)
# else :
#     print('大')

# sum = 0
# for x in range(1, 101):
#     sum += x
# print(sum)

# sum = 0 
# for i in range(2, 101, 2):
#     sum += i
# print(sum)

# from random import randint

# number = randint(1, 10)
# counter = 0
# answer = int(input('请输入你的答案：'))

# while True :
#     if answer < number :
#         answer = int(input('大一点：'))
#         counter += 1
#     elif answer > number :
#         answer = int(input('小一点：'))
#         counter += 1
#     else :
#         print('恭喜你猜对了，答案是:', answer)
#         counter += 1
#         break

# if counter == 1 :
#     print('你真是的个天才！')
# if counter >= 4 :
#     print('不过你太笨了！')

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d * %d = %d' % (i, j, i * j), end = '\t')
#     print()


# import math

# num = int(input('输入一个整数：'))
# flag = int(math.sqrt(num))
# is_Prime = True

# for i in range(2, flag + 1):
#     if (num % i) == 0 :
#         is_Prime = False
#         break
# if is_Prime and num != 1 :
#     print('%d是素数' % num)
# else :
#     print('%d不是素数' % num)


# row = int(input('请输入行数: '))

# for i in range(row):
#     for j in range(i + 1):
#         print('*', end='')
#     print()


# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()

# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()

# 水仙花数
# for i in range(100, 1000) :
#     a = int(i / 100)
#     b = int(i / 10 % 10)
#     c = int(i % 10)
#     if (a**3 + b**3 + c**3) == i :
#         print(i)

# 完全数
# sum = 0
# count = 0
# for num in range(1, 10000):
#     for factor in range(1, num):
#         if num % factor == 0 :
#             sum += factor
#     if sum == num :
#         count += 1
#         print('找到第%d个完全数：%d' % (count, num))
#         sum = 0
#     sum = 0

# 百钱百鸡
# for a in range(0,20):
#     for b in range(0,34):
#         if 7*a + 4*b - 100 == 0 and 100 - a - b >= 0 :
#             print('公鸡%d只，母鸡%d只，小鸡%d只' % (a, b, 100-a-b))

# 斐波那契数列
# a = 0
# b = 1
# c = 0
# while b < 1000 :
#     print(b, end='\t')
#     c = b
#     b = a + b
#     a = c


# a, b = 0, 1
# while a < 1000:
#     print(a)
#     a, b = b, a+b


# craps赌博
# from random import randint 

# player = 0
# c = 0
# money = 1000
# counter = 1000

# while money > 0 :
#     player = randint(1,6) + randint(1,6)
#     if player == 7 or player == 11 :
#         money += counter
#         print('%d点玩家胜，玩家现在有%d元' % (player, money))
#     elif player == 2 or player == 3 or player == 12 :
#         money -= counter
#         print('%d点庄家胜，玩家现在有%d元' % (player, money)) 
#     else :
#         print('%d点游戏继续' % player)
#         while money > 0 :
#             c = player
#             player = randint(1,6) + randint(1,6)
#             if player == c & player != 7:
#                 money += counter
#                 print('%d点玩家胜，玩家现在有%d元' % (player, money))
#             elif player == 7 :
#                 money -= counter
#                 print('%d点庄家胜，玩家现在有%d元' % (player, money))
#             else :
#                 print('%d点游戏继续' % player)
#                 continue   
# print('玩家输光了，游戏结束') 

# import module1
# import module2

# module1.shuchu()


# import os
# import time

# def main():
#     string = '111111111'
#     while True :
#         os.system('cls')
#         print(string)
#         time.sleep(0.2)
#         string = string[1:] + string[0]

# if __name__ == '__main__' :
#     main()

# print(str.upper('abcdefjhijklmnopqrstuvwxyz'))

# from random import randint
# def generate_code(code_len = 8) :
#     """
#     生成指定位数验证码
#     """
#     all_chars = '0123456789abcdefjhijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     result = ''
#     for _ in range(code_len) :
#         result += all_chars[randint(0, last_pos)]

#     return result

# if __name__ == "__main__":
#     print(generate_code(int(input('您需要几位验证码？'))))

# def get_suffix(filename, has_dot=False):
#     """
#     获取文件名的后缀名

#     :param filename: 文件名
#     :param has_dot: 返回的后缀名是否需要带点
#     :return: 文件的后缀名
#     """
#     pos = filename.rfind('.')
#     if 0 < pos < len(filename) - 1:
#         index = pos if has_dot else pos + 1
#         return filename[index:]
#     else:
#         return ''

# if __name__ == "__main__":
#     print(get_suffix('liukuan.pdf', False))

# def max2(x) :
#     (x[0], x[1]) = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0]) 
#     for i in range(2, len(x)) :
#         if x[i] > x[0] :
#             x[1] = x[0] 
#             x[0] = x[i]
#         elif x[i] > x[1] :
#             x[1] = x[i]
#     return (x[0], x[1])

# if __name__ == "__main__":
#     print(max2([1,2,3,6,7,8,34,44,12,3,89]))

# def is_leap(year):
#     result = True
#     if year % 100 != 0 and year % 4 == 0 :
#         result = True
#     elif year % 400 == 0 :
#         result = True
#     else :
#         result = False
#     return result

# def countDay(date = '19000101'):
#     year = int(date[0:4])
#     month = int(date[4:6])
#     day = int(date[6:8])
#     month_day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
#     count = 0

#     for index in range(0, month - 1) :
#         count += month_day[index]
#     count += day
#     if is_leap(year) :
#         count += 1
#     return count

# if __name__ == "__main__":
#     print(countDay(input('请输入8位年月日')))


# from time import sleep
# import os


# class Clock(object):
#     """数字时钟"""

#     def __init__(self, hour=0, minute=0, second=0):
#         """初始化方法

#         :param hour: 时
#         :param minute: 分
#         :param second: 秒
#         """
#         self._hour = hour
#         self._minute = minute
#         self._second = second

#     def run(self):
#         """走字"""
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0

#     def show(self):
#         """显示时间"""
#         return '%02d:%02d:%02d' % \
#                (self._hour, self._minute, self._second)


# def main():
#     clock = Clock(23, 59, 58)
#     while True:
#         os.system('cls')
#         print(clock.show())
#         sleep(1)
#         clock.run()


# if __name__ == '__main__':
#     main()


# def main():
#     list1 = [12, 32, 4, 87, 55, 9, 71, 6]
#     flag = list1[0]
#     for i in list1:
#         if i > flag:
#             flag = i
#     print(flag)

# if __name__ == "__main__":
#     main()

# numbers = [3, 1, 7, 4, 90, 10, 3, 1, 7]
# length = len(numbers)
# numbers.sort()
# i = 0

# while(i < length - 1):
#     if numbers[i] == numbers[i+1]:
#         numbers.remove(numbers[i])
#         length = len(numbers)
#     else :
#         i = i + 1

# print(numbers)

# numbers_mapping = {
#     '1': 'One',
#     '2': 'Two',
#     '3': 'Three',
#     '4': 'Four',
#     '5': 'Five',
#     '6': 'Six',
#     '7': 'Seven',
#     '8': 'Eight',
#     '9': 'Nine',
#     '0': 'Zero'
# }

# input_num = input('Phone:')

# for num in input_num:
#     print(numbers_mapping.get(num, '#'), end = ' ')

# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def play(self):
#         print('%s is playing with the ball' % self.name)
#
#     def sleep(self):
#         print('%s is sleeping' % self.name)
#
#
# class Dog(Pet):
#     def bark(self):
#         print('%s is barking' % self.name)
#
#
# ZhuJiao = Dog('猪脚', '0.5')
# ZhuJiao.play()
# ZhuJiao.sleep()
# ZhuJiao.bark()

# import random
#
#
# def dice():
#     # a = random.randint(1, 6)
#     # b = random.randint(1, 6)
#     # result = (a, b)
#     print((random.randint(1, 6), random.randint(1, 6)))
#
#
# dice()
# import tensorflow as tf
# import numpy as np
# from tensorflow import keras
# model = keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])])
# model.compile(optimizer = 'sgd', loss = 'mean_squared_error')
# xs = np.array([15, 14, 13, 12, 11, 10, 9, 8], dtype = int)
# ys = np.array([8.0, 7.5, 7.0, 6.5, 6.0, 5.5, 5.0, 4.5], dtype = float)
# model.fit(xs, ys, epochs = 1000)
# print(model.predict([7.0]))

# def print_digits(num):
#     ones = num % 10
#     tens = num // 10
#     print("The tens digit is %d, and the ones digit is %d." % (tens, ones))

# print_digits(79)
# import random

# n = random.randint(0, 10)
# print (n)


# def f(x):
#     result = - 5 * x ** 5 + 69 * x ** 2 - 47
#     return result


# print(f(1))
# print(f(2))
# print(f(3))
# print(f(0))


# def future_value(present_value, annual_rate, periods_per_year, years):
#     rate_per_period = annual_rate / periods_per_year
#     periods = periods_per_year * years
#     return present_value * (1 + rate_per_period) ** periods

# print ('$1000 at .02 compounded daily for 3 years yields $%.2f' % future_value(1000, .02, 365, 3))
# import math

# def project_to_distance(point_x, point_y, distance):
#     dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
#     scale = distance / dist_to_origin
#     return point_x * scale, point_y * scale

# print('%.4f %.4f' % project_to_distance(2, 7, 4))

# x = 5

# def a(y):
#     global x
#     x = x + y
#     return x

# def b(x, y):
#     x = x + y
#     return x

# def c(y):
#     return x + y

# def d(y):
#     y = x + y
#     return y

# a(2)
# print(d(1))

# count = 0

# def square(x):
#     global count
#     count += 1
#     return x**2

# print(square(square(square(square(3)))))
# print(count)

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]
print(answer)