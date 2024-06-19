class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merger(left,right):
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else: 
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged
            
        if len(nums1) == 0 and len(nums2) == 0:
            return float(0)
        else:
            call = merger(nums1,nums2)
            mid = len(call)//2
            if len(call)%2 == 0:
                return (call[mid-1]+call[mid])/2
            else:
                return call[mid]
            
        