class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        m = [i*i for i in nums]
        m.sort()
        return m
        