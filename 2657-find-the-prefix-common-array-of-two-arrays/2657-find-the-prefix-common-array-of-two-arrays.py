class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        l = len(A)
        C = []
        for i in range(l):
            x = set(A[:i+1]) & set(B[:i+1])
            C.append(len(x))
        return C