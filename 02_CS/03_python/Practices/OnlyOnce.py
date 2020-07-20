def searchTheOne(string):
    for i in string:
        if string.count(i) == 1:
            return i
    return -1
    
while True:
    try:
        s = input()
        print(searchTheOne(s))
    except:
        break

    
