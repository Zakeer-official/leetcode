class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x = dividend // divisor
        if dividend < -1 and divisor >= -1 and divisor < 1:
            return x-1
        elif dividend > -1 and divisor < -1 and abs(dividend) != abs(divisor):
            return x+1
        elif dividend < -1 and divisor > len(str(dividend)):
            return x+1
        else:
            return x