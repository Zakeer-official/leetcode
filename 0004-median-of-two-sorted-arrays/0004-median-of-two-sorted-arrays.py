class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final = nums1 + nums2
        final.sort()
        return final[len(final)//2] if len(final)%2 != 0 else (final[(len(final)//2)-1]+final[len(final)//2])/2
            
        