class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while 1 <= n <= 100 and 1<= t <= 10:
            if n > 9:
                x = n % 10
                y = n // 10
                if (x * y) % t == 0: return n
            else:
                if n <= t: return t
                else:
                    if n % t == 0: return n
            n = n + 1

        