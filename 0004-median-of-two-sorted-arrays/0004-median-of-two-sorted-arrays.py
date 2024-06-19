class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final = nums1 + nums2
        final.sort()
        if len(nums1) == 0 and len(nums2) == 0:
            return float(0)
        else:
            mid = len(final)//2
            if len(final)%2 == 0:
                return (final[mid-1]+final[mid])/2
            else:
                return final[mid]
            
        