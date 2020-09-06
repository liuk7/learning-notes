n = int(input())
stringSet = []
for i in range(n):
    s = input()
    if len(s) <= 8:
        ss = s.ljust(8, '0')
        stringSet.append(ss)
    else:
        m = len(s) // 8
        for i in range(m):
            stringSet.append(s[i*8:8*(i+1)])
        if s[m*8:]:
            ss = s[m*8:].ljust(8, '0')
            stringSet.append(ss)

print(stringSet)

for e in stringSet:
    print(e)
