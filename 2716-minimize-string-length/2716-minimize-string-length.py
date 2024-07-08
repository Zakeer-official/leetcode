class Solution:
    def minimizedStringLength(self, s: str) -> int:
        x = list(set(sorted(s)))
        y =""
        for i in x:
            y += i
        return len(y)
        