class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        def count(e):
            return nums.count(e),-e
        x = sorted(nums,key= count)
        return x
        