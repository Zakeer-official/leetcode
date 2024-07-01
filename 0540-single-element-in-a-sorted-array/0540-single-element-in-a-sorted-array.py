class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(1,len(nums)+1):
            if nums.count(nums[i-1]) == 1:
                return nums[i-1]