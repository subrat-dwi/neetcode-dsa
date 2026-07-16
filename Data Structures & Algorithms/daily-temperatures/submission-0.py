class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        st = []
        result = [0]*l

        for i in range(l):
            while st and temperatures[i] > temperatures[st[-1]]:
                j = st.pop()
                result[j] = i-j
            st.append(i)

        return result