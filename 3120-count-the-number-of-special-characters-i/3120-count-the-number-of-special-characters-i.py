class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        letters = sorted(set(word))
        for i in range(len(letters)):
            if letters[i].lower() in letters[i+1:]:
                count += 1
        return count

        