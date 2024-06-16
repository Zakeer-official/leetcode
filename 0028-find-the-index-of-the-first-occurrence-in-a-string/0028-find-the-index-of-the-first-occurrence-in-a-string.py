class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = []
        m = ''
        for i in range(len(haystack)):
            for j in range(i,len(haystack)):
                m += haystack[j]
                if (j-i)%len(needle) == len(needle) - 1 :
                    l.append(m)
                    m = ''
                    break
        for i in range(len(l)) :
            if l[i] == needle :
                return i
                break
        return -1