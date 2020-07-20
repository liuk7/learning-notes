def isAutomorphic(num):
    cube = str(num ** 2)
    n = len(str(num))
    if cube[-n:] == str(num):
        return True
    else:
        return False

while True:
    try:
        n = int(input())
        count = 0
        for i in range(n+1):
            if isAutomorphic(i):
                count += 1
        print(count)
    except:
        break