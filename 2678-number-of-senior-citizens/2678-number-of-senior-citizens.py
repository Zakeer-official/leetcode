class Solution:
    def countSeniors(self, details: List[str]) -> int:
        st = []
        count = 0
        for i in details:
            st.append(int(i[11:13]))
        for i in st:
            if i > 60:
                count += 1
        return count

        