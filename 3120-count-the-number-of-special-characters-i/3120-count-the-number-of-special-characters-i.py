class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c = 0
        car = sorted(set(word))
        for i in range(len(car)):
            if car[i].lower() in car[i+1:]:
                c += 1
        return c

        