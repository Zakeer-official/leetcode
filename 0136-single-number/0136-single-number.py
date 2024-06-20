class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        y = list(set(nums))
        x = 0
        for i in y:
            if nums.count(i) == 1:
                return i 
        