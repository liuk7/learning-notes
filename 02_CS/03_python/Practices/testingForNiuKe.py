# from collections import defaultdict
 
# dd, s, res = defaultdict(list), input(), ""
# for i in set(s):
#     dd[s.count(i)].append(i)

# for i in sorted(dd.keys(), reverse=True):
#     res += "".join(sorted(dd[i], key=ord))

# print(res)


# while True:
#     try:
#         houn = input()
#         hou_l = input().split()
#         piaon= int(input())
#         piao_l = input().split()
#         youxiao =0
#         for i in hou_l:
#             if i in piao_l:
#                 print(i +" : "+str(piao_l.count(i)))
#                 youxiao += piao_l.count(i)
#             else:
#                 print(i +" : "+str(piao_l.count(i)))
#         print('Invalid : '+str(piaon-youxiao))
                 
#     except:
#         break

# def is_prime(n):
#     m = int(n ** (1/2)) if  int(n ** (1/2)) > 2 else 2
#     for i in range(2, m+1):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(3))

# print('aaa'.ljust(8, '0'))

# sortedString = input()
# countChar = {}

# for c in sortedString:
#     if c.isalpha() or c.isdigit() or c.isspace():
#         if c not in countChar.keys():
#             countChar[c] = 1
#         else:
#             countChar[c] += 1

# countChar = dict(sorted(countChar.items(), key=lambda x:x[0]))
# print(countChar)

# stringValue = sorted(countChar.items(), key=lambda x:x[1], reverse=True)
# print(stringValue)

# result = ""
# for _ in stringValue:
#     result += _[0]

# print(result)

