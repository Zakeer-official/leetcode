class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = set(nums)
        y = sorted(list(x))
        return y[-3] if len(y) >= 3 else y[-1]
        