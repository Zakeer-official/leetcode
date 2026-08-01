class Solution:
    def predictTheWinner(self, A: List[int]) -> bool:
        n = len(A)
        if ~n & 1: return True

        dp = [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = A[i]
            for j in range(i + 1, n):
                dp[j] = max(A[i] - dp[j], A[j] - dp[j - 1])

        return dp[n - 1] >= 0