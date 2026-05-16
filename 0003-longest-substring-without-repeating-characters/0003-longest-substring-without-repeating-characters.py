class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = ""
        y = 0
        for i in s:
            if i in x:
                x = x[x.index(i)+1:]
            x += i
            y = max(len(x),y)
        return y


        