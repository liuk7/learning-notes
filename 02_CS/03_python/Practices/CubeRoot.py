def cubeRoot(num):
    Min = 0
    Max = num
    Mid = 0
    while (Max - Min) > 0.000001:
        Mid = (Max + Min) / 2
        if Mid * Mid * Mid > num:
            Max = Mid
        elif Mid * Mid * Mid < num:
            Min = Mid
        else:
            return Mid
        print(Max, Mid, Min)
    return Max


while True:
    try:
        Num = int(input())
        print("%.1f" % cubeRoot(Num))
    finally:
        break
