class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myst = set(nums)
        if (len(nums) == len(myst)):
            return False
        else:
            return True
