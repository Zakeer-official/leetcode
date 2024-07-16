class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = {}
        for i in strs:
            j = "".join(sorted(i))
            if j not in x:
                x[j] = []
            x[j].append(i)
        y = list(x.values())
        return y