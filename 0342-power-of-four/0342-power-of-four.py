class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        l = [4**x for x in range(16)]
        return n in l
        