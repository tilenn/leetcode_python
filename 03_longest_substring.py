import enum


def lengthOfLongestSubstring(s):
    appearances = {}

    longest_substring = 0

    start_idx = 0
    end_idx = 0

    for i, s in enumerate(s):
        end_idx = i
        if s not in appearances.keys():
            appearances[s] = i
        else:
            start_idx = max(appearances[s] + 1, start_idx)
            appearances[s] = i
        longest_substring = max(end_idx - start_idx + 1, longest_substring)

    return longest_substring


case_1 = "abcabcbb"
case_2 = "bbbbb"
case_3 = "pwwkew"
case_4 = "aab"
case_5 = "dvdf"
case_6 = "abba"

print(lengthOfLongestSubstring(case_1))
print(lengthOfLongestSubstring(case_2))
print(lengthOfLongestSubstring(case_3))
print(lengthOfLongestSubstring(case_4))
print(lengthOfLongestSubstring(case_5))
print(lengthOfLongestSubstring(case_6))
