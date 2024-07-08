class Solution:
    def minimizedStringLength(self, s: str) -> int:
        x = list(set(sorted(s)))
        return len(x)
        