class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        maxi = 0

        for i in range(0, l):
            min_h = heights[i]
            for j in range(i, l):
                min_h = min(min_h, heights[j])
                w = j-i+1
                area = min_h*w
                maxi = max(maxi, area)

        return maxi