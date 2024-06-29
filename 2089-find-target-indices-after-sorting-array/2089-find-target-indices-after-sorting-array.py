class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        def merge(l, r):
            merged = []
            i = j = 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    merged.append(l[i])
                    i += 1 
                else:
                    merged.append(r[j])
                    j += 1
            merged.extend(l[i:])
            merged.extend(r[j:])
            return merged
                
        def ms(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = ms(arr[:mid])
            right = ms(arr[mid:])
            return merge(left, right)
        y = ms(nums)
        result = []
        for i in range(len(y)):
            if target == y[i]:
                result.append(i)
        return result
        