class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = set(nums)
        y = list(x)
        def merge_sort(y):
            if len(y) <= 1:
                return y
            mid = len(y) // 2
            left = y[:mid]
            right = y[mid:]
            left = merge_sort(left)
            right = merge_sort(right)
            return merge(left, right)
        def merge(left, right):
            result = [] 
            i = j = 0 
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        y = merge_sort(y)
        return y[-3] if len(y) >= 3 else y[-1]
        