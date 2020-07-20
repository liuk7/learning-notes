import math

def is_prime(n):
    m = int(math.sqrt(n)) + 1
    for i in range(2, m):
        if n % i == 0:
            return False
    return True

while True:
    try:
        even = int(input())
        even_half = even // 2
        index = 0
        for index in range(even_half):
            if is_prime(even_half - index) and is_prime(even_half + index):
                print(even_half - index)
                print(even_half + index)
                break
    except:
        break 