class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        l = []
        for i in arr: 
            if arr.count(i) == 1: l.append(i)
        return l[k-1] if len(l) >= k else ""
        