class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = set(nums)
        y = list(x)
        x = 0
        for i in y:
            if nums.count(i) == 1:
                x = i
        return x
        