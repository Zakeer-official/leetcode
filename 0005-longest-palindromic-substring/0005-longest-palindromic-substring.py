class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        l = s[0]
        for i in range(len(s)):
            x = s[i]
            for j in range(i+1,len(s)):
                x  += s[j]
                if x != x[::-1]:
                    if len(x) == len(s):
                        x = x[:-1]
                    continue
                if x == x[::-1]:
                    if len(x) > len(l):
                        l = x
        return l

        