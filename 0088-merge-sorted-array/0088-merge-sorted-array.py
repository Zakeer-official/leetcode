class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
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
            
        if len(nums1)==0 and len(nums2) == 0:
            print(nums1)
        else:
            call = merger(nums1[0:m],nums2[0:n])
            for i in range(len(call)):
                nums1[i] = call[i]
            print(nums1)
            