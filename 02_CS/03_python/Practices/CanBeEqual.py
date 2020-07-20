def searchEqual(l, target):
    if target == 0:
        return True
    
    elif not l:
        return False

    else:
        tar = target - l[0]
        return searchEqual(l[1:], target) or searchEqual(l[1:], tar)


while True:
    try:
        length = int(input())
        numbers = list(map(int, input().split()))

        five = []
        three = []
        others = []

        for e in numbers:
            if e % 5 == 0:
                five.append(e)
            elif e % 3 == 0:
                three.append(e)
            else:
                others.append(e)

        diff_1 = abs(sum(five) - sum(three))
        diff_2 = sum(others) - diff_1

        if diff_2 % 2 != 0:
            print('false')
        else:
            print(str(searchEqual(others, diff_2 / 2)).lower())
    except:
        break
