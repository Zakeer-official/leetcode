class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        sorted_words = sorted(words, key=lambda x: int(x[-1]))
        x = []
        for i in sorted_words:
            x.append(i[:-1])
        return ' '.join(x)