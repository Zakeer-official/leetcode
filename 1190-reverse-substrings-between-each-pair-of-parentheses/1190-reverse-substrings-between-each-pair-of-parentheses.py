class Solution:
    def reverseParentheses(self, s: str) -> str:
        lst = list(s)
        x = []
        for i in lst:
            if i == ')':
                sor = ""
                while x[-1] != '(':
                    sor += x.pop()
                x.pop()
                sort = list(sor)
                x.extend(sort)
            else:
                x.append(i)
        x = "".join(x)
        return x
        