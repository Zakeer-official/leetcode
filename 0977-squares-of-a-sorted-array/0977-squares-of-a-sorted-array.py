class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        y = [lambda x=x: x*x for x in nums]
        m= [func() for func in y]
        m.sort()
        return m
        