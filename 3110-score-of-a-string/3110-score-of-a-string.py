class Solution:
    def scoreOfString(self, s: str) -> int:
        x = 0
        sum = 0
        while  x < len(s)-1:
            sum += abs(ord(s[x]) - ord(s[x+1]))
            x += 1
        return sum
        