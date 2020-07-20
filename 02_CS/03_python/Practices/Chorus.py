def getLIS(n, nums):
    length_1 = [1]*n
    length_2 = [1]*n

    if not nums:
        return [], []

    #从左到右寻找最大上升子串
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and length_1[i] < length_1[j] + 1:
                length_1[i] = length_1[j] + 1

    #从右到左寻找最大上升子串
    for i in range(n-1, -1, -1):
        for j in range(i+1,n):
            if nums[j] < nums[i] and length_2[i] < length_2[j] + 1:
                length_2[i] = length_2[j] + 1

    return length_1, length_2
   


while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        l1, l2 = getLIS(n, nums)
        res = 0

        # print(l1)
        # print(l2)


        for i in range(n):
            if l1[i] + l2[i] > res:
                res = l1[i] + l2[i]

        print(n - res + 1)
    
    except:
        break
