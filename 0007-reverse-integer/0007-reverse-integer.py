class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        if y[0] == '-' and y[-1] == '0':
            z = y.rstrip('0')
            if z == '':
                return 0
            out = -int(z[:0:-1])
        elif y[0] == '-' and y[-1] != '0':
            out = -int(y[:0:-1])
        elif y[0] != '-' and y[-1] == '0':
            z = y.rstrip('0')
            if z == '':
                return 0
            out = int(z[::-1])
        else:
            out = int(y[::-1])
        
        if out < -2**31 or out > 2**31 - 1:
            return 0
        return out