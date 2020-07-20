def reverseString(str1):
    str = list(str1)
    length = len(str)

    if length % 2 == 0:
        flag = int(length / 2)
    else:
        flag = int(length // 2 + 1)

    for i in range(flag):
        str[i], str[length-i-1] = str[length-i-1], str[i]

    return str

while True:
    try:      
        str = input()
        print("".join(reverseString(str)))
    except:
        break

# print(input()[::-1])