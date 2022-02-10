def isPalindrome(x):
    if x < 0:
        return False

    tmp = x
    res = 0
    while tmp:
        res = (res * 10) + (tmp % 10)
        tmp = int(tmp / 10)

    return res == x


print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(11311))
