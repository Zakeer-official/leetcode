class Solution:
    def isValid(self, s: str) -> bool:
        
        d ={"]" : "[", ")" : "(", "}":"{"}

        l = []
        if len(s) != 0:
            for i in range(len(s)):
                if len(s)%2 == 0:
                    if s[i] in list(d.values()):
                        l.append(s[i])
                    elif s[i] in list(d.keys()):
                        if l and d[s[i]] == l[-1]:
                            l.pop()
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        return True if len(l) == 0 else False