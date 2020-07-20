def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def lcm(c, d):
    return c * d // gcd(c, d)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
