class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        sorted_words = sorted(words, key=lambda x: int(x[-1]))
        sorted_sentence = ' '.join(word[:-1] for word in sorted_words)
        return sorted_sentence