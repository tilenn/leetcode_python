def intToRoman(num):
    res = ""
    roman_numerals = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

    # 1000
    thousands = num // 1000
    res = thousands * roman_numerals[1000]
    num = num % 1000

    # 100
    hundreds = num // 100

    tmp = hundreds // 5
    tmp_2 = hundreds % 5

    if tmp == 0:
        if tmp_2 < 4:
            res += roman_numerals[100] * tmp_2
        else:
            res += roman_numerals[100] + roman_numerals[500]
    else:
        if tmp_2 < 4:
            res += roman_numerals[500] + tmp_2 * roman_numerals[100]
        else:
            res += roman_numerals[100] + roman_numerals[1000]
    num = num % 100

    # 10

    ten = num // 10

    tmp = ten // 5
    tmp_2 = ten % 5

    if tmp == 0:
        if tmp_2 < 4:
            res += roman_numerals[10] * tmp_2
        else:
            res += roman_numerals[10] + roman_numerals[50]
    else:
        if tmp_2 < 4:
            res += roman_numerals[50] + tmp_2 * roman_numerals[10]
        else:
            res += roman_numerals[10] + roman_numerals[100]
    num = num % 10

    # 1

    one = num

    tmp = one // 5
    tmp_2 = one % 5

    if tmp == 0:
        if tmp_2 < 4:
            res += roman_numerals[1] * tmp_2
        else:
            res += roman_numerals[1] + roman_numerals[5]
    else:
        if tmp_2 < 4:
            res += roman_numerals[5] + tmp_2 * roman_numerals[1]
        else:
            res += roman_numerals[1] + roman_numerals[10]

    return res


print(intToRoman(3225))
print(intToRoman(1994))
