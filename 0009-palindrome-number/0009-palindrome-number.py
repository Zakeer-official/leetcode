class Solution:
    def isPalindrome(self, x: int) -> bool:
        fing = str(x)
        left = 0
        right = len(fing) - 1

        if fing[left] == '-':
            return False

        while left < right:
            if fing[left] != fing[right]:
                return False
            left += 1
            right -= 1
        return True

# set = Solution()
# x = int(input())
# print(set.isPalindrome(x))
