class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [(names[i], heights[i]) for i in range(len(names))]
        sorted_people = sorted(people, key=lambda x: -x[1])
        sorted_names = [i[0] for i in sorted_people]
        return sorted_names