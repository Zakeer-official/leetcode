class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def quick(low,high):
            pivot = nums[high]
            i = low - 1
            for j in range(low,high):
                if nums[j] <= pivot:
                    i += 1 
                    nums[i],nums[j] = nums[j],nums[i]
            nums[i+1],nums[high] = nums[high],nums[i+1]
            return i+1
        def qs(low,high):
            if low < high:
                pi = quick(low,high)
                qs(low,pi-1)
                qs(pi+1,high)
        qs(0,len(nums)-1)