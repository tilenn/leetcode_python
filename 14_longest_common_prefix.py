def longestCommonPrefix(strs):
    longest_prefix = ""

    for i in range(len(strs[0])):
        for word in strs:
            if i == len(word) or word[i] != strs[0][i]:
                return longest_prefix
        longest_prefix += strs[0][i]

    return longest_prefix


print(longestCommonPrefix(["flower", "flow", "flight", "fil"]))
print(longestCommonPrefix(["aaa", "aa", "aaa"]))
