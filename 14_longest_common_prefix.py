def longestCommonPrefix(strs):
    longest_prefix = strs[0]

    for word in strs:
        if word == "":
            longest_prefix = ""
            continue
        for i in range(0, min(len(longest_prefix), len(word))):
            # print(i)
            if longest_prefix[i] != word[i]:
                longest_prefix = word[:i]
                break
            if i == min(len(longest_prefix), len(word)) - 1 and len(word) < len(
                longest_prefix
            ):
                longest_prefix = word

    return longest_prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["aaa", "aa", "aaa"]))
