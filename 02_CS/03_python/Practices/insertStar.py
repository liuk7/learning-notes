while True:
    try:
        nums = input()
        res = ''
        isNum = False

        for a in nums:
            if a.isdigit():
                if not isNum:
                    res = res + '*' + a
                else:
                    res = res + a
                isNum = True
            else:
                if isNum:
                    res = res + '*' + a
                else:
                    res = res + a
                isNum = False

        if nums[-1].isdigit():
            print(nums[-1])
            print(True)
            res += '*'

        print(res)
                    
    except:
        break