class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = int("".join(map(str,digits))) + 1
        return [int(i) for i in str(x)]
        