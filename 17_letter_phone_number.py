def letterCombinations(digits):
    if len(digits) == 0:
        return []
    arr = []
    build_combinations(digits, "", arr)
    return arr


num_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def build_combinations(digits, str, arr):
    if digits == "":
        arr.append(str)
        return str

    tmp = str[:]
    for letter in num_to_letters[digits[0]]:
        tmp += letter
        build_combinations(digits[1:], tmp, arr)
        tmp = str


print(letterCombinations("234"))
print(letterCombinations(""))
# print(letterCombinations("2"))
