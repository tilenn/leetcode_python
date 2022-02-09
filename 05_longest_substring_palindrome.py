def longestPalindrome(s):
    najdaljsi = ""
    len_najdaljsi = 0

    # vsako crko razsirimo naprej levo in desno
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len_najdaljsi:
                najdaljsi = s[l : r + 1]
                len_najdaljsi = r - l + 1
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len_najdaljsi:
                najdaljsi = s[l : r + 1]
                len_najdaljsi = r - l + 1
            l -= 1
            r += 1
    return najdaljsi


print(longestPalindrome("bb"))
