"""
题目解析：
有两种情况
1: m小于n，那么可定有n-m个盘子注定没有苹果，于是返回f(m, m)
2: 至少一个盘子里没有苹果，那么返回f(m, n-1)
3: 所有盘子里都至少有一个苹果，那么问题就变成了m-n个苹果在n个盘子里分配，返回f(m-n, n)
其中2，3加起来就是所有情况
"""

def putApples(m, n):
    if m == 0 or n == 1:
        return 1
    elif n > m:
        return putApples(m, m)
    else:
        return putApples(m, n - 1) + putApples(m - n, n)

while True:
    try:
        list = input().split()
        res = putApples(int(list[0]), int(list[1]))
        print(res)
    except:
        break

