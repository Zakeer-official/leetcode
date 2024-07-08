class Solution:
    def minimizedStringLength(self, s: str) -> int:
        x = []
        for i in s:
            if i not in x:
                x.append(i)
        return len(x)
        