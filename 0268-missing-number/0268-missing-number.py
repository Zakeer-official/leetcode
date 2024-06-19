class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        for i in range(len(nums)+1):
            if i not in nums:
                x = i
        return x
        