def convert(s, numRows):
    if numRows == 1:
        return s
    res = ""
    step = 2 * (numRows - 1)

    for row in range(numRows):
        for i in range(row, len(s), step):
            # print(s[i])
            res += s[i]
            # ce nismo v prvi ali zadnji
            if 0 < row < numRows - 1 and i + step - 2 * row < len(s):
                res += s[i + step - 2 * row]
    return res


print(convert("PAYPALISHIRING", 4))
