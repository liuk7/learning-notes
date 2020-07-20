# def is_sub(l1, l2):
#     if not l1 or not l2:
#         return -1

#     n1, n2 = len(l1), len(l2)

#     #从右到左寻找子序列
#     i = n1 - 1
#     j = n2 - 1
#     while j > -1:
#         while i > -1:
#             if l1[i] == l2[j] and i == 0:
#                 return j
#             if l1[i] == l2[j] and i != 0:
#                 i -= 1
#                 j -= 1
#             else:
#                 j -= 1

#     return -1

# while True:
#     try:

#         l1 = input()
#         l2 = input()
#         print(is_sub(l1, l2))

#     except:
#         break

def find_me(m, n, target, source):
    if not source:
            return -1

    i = 0 
    k = 0 
    t = len(target)

    while i < m * n:
        if k > t - 1:
            break
        if target[k] == source[i]:
            if k == 0:
                res = i
            k += 1
            i += 1
        else:
            i += 1

    print(k)
    print(res)


    if k == t:
        return res
    else:
        return -1

m, n = map(int, input().split())
target = input()
source = ''
for i in range(m):
    line = list(input())
    for e in line:
        source += e
print(source)

res = find_me(m, n, target, source)

print(str(res // 5) + " " + str(res % 5))