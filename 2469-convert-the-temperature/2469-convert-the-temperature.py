class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        x = []
        x.append(celsius + 273.15)
        x.append(((celsius*9)/5)+32)
        return x
        