class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        x = sorted(set(nums1) & set(nums2))
        if len(x) == 0: 
            return -1
        else: 
            return x[0]
            