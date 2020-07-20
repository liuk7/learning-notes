def stringNum(string1, string2):
    if not string1 or not string2:
        return 0

    n = len(string2)
    count = 0
    string11 = string1.replace(' ', '')

    i = 0
    while i < len(string11):
        if string11[i] == string2[0]:
            if string11[i:i+n] == string2:
                count += 1
        i += 1
    return count

while True:
    try:
        string1 = input()
        string2 = input()
        print(stringNum(string1, string2))
    except:
        break
