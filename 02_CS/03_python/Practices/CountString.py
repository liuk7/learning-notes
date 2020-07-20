while True:
    try:
        # rawString = input()
        # sortedString = sorted(rawString)
        sortedString = input()
        countChar = dict()

        for c in sortedString:
            if c.isalpha() or c.isdigit() or c.isspace():
                if c not in countChar.keys():
                    countChar[c] = 1
                else:
                    countChar[c] += 1

        countChar = sorted(countChar.items(), key=lambda x:x[0])
        stringValue = sorted(countChar.items(), key=lambda x:x[1], reverse=True)

        result = ""
        for _ in stringValue:
            result += _[0]

        print(result)
        
    except:
        break