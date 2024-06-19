class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = set(nums)
        y = list(x)
        for i in range(len(y)):
            min_id = i 
            for j in range(i+1,len(y)):
                if y[min_id] > y[j] :
                    min_id = j
            y[min_id] , y[i] = y[i] , y[min_id]
        return y[-3] if len(y) >= 3 else y[-1]
        