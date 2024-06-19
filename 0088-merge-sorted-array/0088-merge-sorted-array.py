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
        def mer(nums1,nums2):
            if len(nums1)==0 and len(nums2) == 0:
                print(nums1)
            elif len(nums1)==0 and len(nums2) > 0:
                nums2.sort()
                print(nums2)
            elif len(nums1) > 0 and len(nums2) == 0:
                nums1.sort()
                print(nums1)
            else:
                call = merger(nums1[0:m],nums2[0:n])
                for i in range(len(call)):
                    nums1[i] = call[i]
                print(nums1)
        mer(nums1,nums2)
            