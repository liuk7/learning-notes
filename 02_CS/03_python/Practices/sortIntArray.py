def sortIntArray(num, intArray, flag):
    # flag为0从小到大，为1从大到小
    if flag:
        quickSortRe(intArray, 0, num - 1)
    else:
        quickSort(intArray, 0, num - 1)
    

def quickSort(array, low, high):
    #从小到大排序
    if low < high:
        key = array[low]
        r = high
        l = low

        while low < high:
            while low < high and key < array[high]:
                high -= 1
            array[low] = array[high]
            while low < high and key > array[low]:
                low += 1
            array[high] = array[low]
        array[low] = key
        quickSort(array, l, low - 1)
        quickSort(array, high + 1, r)


def quickSortRe(array, low, high):
    #从大到小排序
    if low < high:
        key = array[low]
        l = low
        r = high

        while low < high:
            while low < high and key > array[high]:
                high -= 1
            array[low] = array[high]
            while low < high and key < array[low]:
                low += 1
            array[high] = array[low]
        array[low] = key
        quickSortRe(array, l, low - 1)
        quickSortRe(array, high + 1, r)

while True:
    try:
        num = int(input())
        array = list(map(int, input().split()))
        flag = int(input())
        sortIntArray(num, array, flag)
        for e in array:
            print(str(e) + ' ', end='')
    except:
        break
