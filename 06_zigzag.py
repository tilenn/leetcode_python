def convert(s, numRows):
    if len(s) <= numRows or numRows == 1:
        return s
    step = 2 * numRows - 2
    formatted_str = ""
    idx = step
    for i in range(numRows):
        for j in range(len(s) // numRows + 1):
            print(i + j * step)
            if i + j * step < len(s):
                formatted_str += s[i + j * step]

            if i != 0 and i != numRows - 1:
                # print(idx + j * step)
                if idx + j * step < len(s):
                    formatted_str += s[idx + j * step]
        idx -= 1
    # print(formatted_str)
    return formatted_str


# def printVmes(s, numRows):
#     step = 2 * numRows - 2
#     formatted_str = ""
#     idx = step - 1
#     for j in range(numRows):
#         if j != 0 and j != numRows - 1:
#             for i in range(numRows):
#                 if idx + i * step < len(s):
#                     formatted_str += s[idx + i * step]
#             idx -= 1
#     print(formatted_str)


print(convert("PAYPALISHIRING", 2))
# printVmes("PAYPALISHIRING", 3)
# printVmes("a", 3)
