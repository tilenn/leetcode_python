def myAtoi(s):
    MIN = -(2**31)
    MAX = 2**31 - 1

    res = 0

    # nam pove ali je plus ali minus
    sign = False
    # nam pove ali smo + ali minus ze videli
    sign_read = False
    # nam pove ali trenutno beremo stevilo
    reading_num = False

    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for letter in s:

        # vidimo whitespace, ce smo do sedaj brali stevilo -> BREAK
        # cene nadaljujemo
        if letter == " ":
            if reading_num or sign_read:
                break
            continue

        # vidimo minus
        # ce smo ga ze prebrali, ali smo do sedaj brali stevilo -> BREAK
        if letter == "-":
            if reading_num or sign_read:
                break
            sign = True
            sign_read = True
            continue

        if letter == "+":
            if reading_num or sign_read:
                break
            sign_read = True
            continue

        if letter not in digits:
            break

        if letter in digits:
            reading_num = True
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
