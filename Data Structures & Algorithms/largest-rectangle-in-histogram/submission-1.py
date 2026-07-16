class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        l = len(heights)
        maxi = 0
        st = []

        for i in range(l):
            while st and heights[i] < heights[st[-1]]:
                j = st.pop()
                w = i - st[-1] - 1 if st else i
                area = heights[j] * w
                maxi = max(maxi, area)
            st.append(i)

        return maxi