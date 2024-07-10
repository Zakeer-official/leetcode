class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = []
        if len(nums1) > len(nums2):
            for i in range(len(nums2)):
                for j in range(len(nums1)):
                    if nums2[i] == nums1[j]:
                        x.append(nums2[i])
                        nums1.remove(nums1[j])
                        break
        else:
            for i in range(len(nums1)):
                for j in range(len(nums2)):
                    if nums1[i] == nums2[j]:
                        x.append(nums1[i])
                        nums2.pop(j)
                        break
        return x
        