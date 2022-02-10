def romanToInt(s):
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    flag = False
    for i, letter in enumerate(s):
        if flag:
            flag = False
            continue
        if letter == "M":
            num += roman_numerals[letter]

        elif (
            i + 1 < len(s)
            and 1 < (roman_numerals[s[i + 1]] // roman_numerals[letter]) <= 10
        ):
            num += roman_numerals[s[i + 1]] - roman_numerals[letter]
            flag = True
        else:
            num += roman_numerals[letter]
        # print(i, letter, num)
    return num


print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
