class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = [i for i in nums if nums.count(i) == 1]
        return x[0]
        