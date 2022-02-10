def myAtoi(s):
    MIN = -(2**31)
    MAX = 2**31 - 1

    res = 0
    sign = False
    sign_read = False
    flag = False
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for letter in s:
        # print("letter:", letter)
        if letter == " ":
            if flag:
                break
            if res == 0:
                continue
            else:
                break

        if letter == "-":
            if flag:
                break
            flag = True
            if sign_read:
                break
            else:
                sign = True
                sign_read = True
                continue

        if letter == "+":
            if flag:
                break
            flag = True
            if sign_read:
                break
            else:
                sign_read = True
                continue

        if letter not in digits:
            break

        if letter in digits:
            flag = True
            res = (res * 10) + int(letter)
    res = -res if sign else res

    if res > MAX:
        res = MAX
    elif res < MIN:
        res = MIN

    return res


print(myAtoi("42"), "expected 42")
print(myAtoi("   -42"), "expected -42")
print(myAtoi("4193 with words"), "expected 4193")
print(myAtoi("3.14158"), "expected 3")
print(myAtoi("+-12"), "expected 0")
