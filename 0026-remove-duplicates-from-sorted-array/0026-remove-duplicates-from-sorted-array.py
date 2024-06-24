class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = set()
        i = 0
        while i < len(nums):
            if nums[i] not in x:
                x.add(nums[i])
                i += 1
            else:
                nums.pop(i)
        return len(nums)