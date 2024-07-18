class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l,r = 0,len(nums) - 1
        nums = sorted(nums)
        while l <= r:
            mid = l + (r - l) // 2
            if target > nums[mid]: l = mid + 1
            elif target < nums[mid]: r = mid - 1
            else: return mid
        return -1


        