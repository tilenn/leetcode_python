def reverse(x):
    res = 0
    tmp = x if x > 0 else -x
    while tmp != 0:
        res *= 10
        res += tmp % 10
        tmp = tmp // 10
    if res < -(2**31) or res > 2**31 + 1:
        return 0
    return res if x > 0 else -res


print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(1534236469), "1534236469"[::-1])
