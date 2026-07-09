class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left, max_right = 0, 0
        left, right = 0, n-1
        trapped = 0

        while left < right:

            if height[left] <= height[right]:
                if height[left] < max_left:
                    trapped += max_left - height[left]
                else:
                    max_left = height[left]
                left += 1

            else:
                if height[right] < max_right:
                    trapped += max_right - height[right]
                else:
                    max_right = height[right]
                right -= 1

        return trapped

