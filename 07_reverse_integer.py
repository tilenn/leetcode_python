import math


def reverse(x):
    MIN = int(-(2**31))  # -2^31,
    MAX = int(2**31 - 1)  #  2^31 - 1

    res = 0
    while x:
        zadnja_cifra = int(math.fmod(x, 10))
        x = int(x / 10)

        if res > MAX // 10 or (res == MAX // 10 and zadnja_cifra >= MAX % 10):
            return 0
        if res < MIN // 10 or (res == MIN // 10 and zadnja_cifra <= MIN % 10):
            return 0
        res = (res * 10) + zadnja_cifra

    return res


print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(1534236469), "1534236469"[::-1])
