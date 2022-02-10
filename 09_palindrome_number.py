def isPalindrome(x):
    if x < 0:
        return False

    tmp = x
    res = 0
    while tmp:
        res = (res * 10) + (tmp % 10)
        tmp = int(tmp / 10)

    return res == x


def isPalindrome_v2(x):
    if x < 0:
        return False

    div = 1
    while x >= 10 * div:
        div *= 10

    while x:
        r = x % 10
        l = x // div

        if l != r:
            return False

        x = (x % div) // 10
        div = div // 100

    return True


print(isPalindrome_v2(121))
print(isPalindrome_v2(-121))
print(isPalindrome_v2(11311))
