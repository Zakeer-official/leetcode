class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) == len(s):
            for i in s:
                if i in t:
                    t = t.replace(i,"",1)
        else:
            return False
        return len(t) == 0