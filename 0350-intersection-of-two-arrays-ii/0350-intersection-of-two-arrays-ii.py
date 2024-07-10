class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = []
        nums1.sort()
        nums2.sort()
        if len(nums1) > len(nums2):
            for i in nums2:
                for j in nums1:
                    if i == j:
                        x.append(i)
                        nums1.remove(j)
                        break
        else:
            for i in nums1:
                for j in nums2:
                    if i == j:
                        x.append(i)
                        nums2.remove(j)
                        break
        return x
        