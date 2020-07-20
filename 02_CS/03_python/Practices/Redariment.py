###
#
# 方法一：动态规划
# 遍历数组nums，对于每一个nums[i]，都要用nums[i]之前的数字和它比较，如果nums[i]大于nums[j]，则更新length[i]=max(length[i], length[j] + 1)
# 初始的length[i] = 1
#
###

# def getLIS(a, numbers):
#     length = []
#     if not numbers:
#         return 0

#     for i in range(a):
#         length.append(1)
#         for j in range(i):
#             if numbers[i] > numbers[j]:
#                 length[i] = max(length[i], length[j] + 1)
#     return max(length)

# while True:
#     try:
#         a = int(input())
#         numbers = list(map(int, input().split()))
#         print(getLIS(a, numbers))
#     except:
#         break

###
#
# 方法二：贪心+二分查找
# 对于数组nums，维护一个d[i]，表示长度为i的最长上升子序列的末尾元素的最小值，用length表示该子序列的长度
# 遍历数组nums，对于每一个nums[i]，如果nums[i] > d[length]，则更新length = length + 1， d.append(nums[i])
# 否则，用二分查找，找到d[j]，使得d[j-1] < nums[i] < d[j]，并更新d[j] = nums[i]
# 
###
def getLIS(a, numbers):
    d = []
    for n in numbers:
        if not d or  d[-1] < n:
            d.append(n)
        else:
            binarySearch(d, n)

    return len(d)



def binarySearch(d, num):
    l = 0
    r = len(d) - 1
    mid = 0
    loc = r
    while r >= l:
        mid = (l + r) // 2
        if num <= d[mid]:
            loc = mid
            r = mid - 1
        else:
            l = mid + 1
    d[loc] = num
    return d


while True:
    try:
        a = int(input())
        numbers = list(map(int, input().split()))
        print(getLIS(a, numbers))
    except:
        break
