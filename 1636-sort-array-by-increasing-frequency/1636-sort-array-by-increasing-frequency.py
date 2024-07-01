class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        def count(e):
            return nums.count(e),100-e
        x = sorted(nums,key= count)
        return x
        