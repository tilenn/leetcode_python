def longestPalindrome(s):
    # pogledamo vse substringe dolzine len(s), itd.
    start_idx = 0

    # len(s) - x == koliko je substringu dolzine x
    x = len(s)

    while True:
        # substring dolzine 0 ni relevanten
        if x == 0:
            break
        for i in range(len(s) - x + 1):
            # substring in preverimo ali je polindrom
            tmp = s[start_idx + i : start_idx + x + i]
            tmp_rev = tmp[::-1]

            if tmp == tmp_rev and tmp_rev in tmp:
                return tmp
        x = x - 1

    return s


case_1 = "babad"
case_2 = "cbbd"

print(longestPalindrome(case_1))
print(longestPalindrome(case_2))
