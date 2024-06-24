class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = []
        i = 0
        while i < len(nums):
            if nums[i] not in x:
                x.append(nums[i])
                i += 1
            else:
                nums.pop(i)
        return len(nums)