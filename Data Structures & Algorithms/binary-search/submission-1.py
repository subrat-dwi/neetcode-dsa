class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)

        left, right = 0, l

        while left<right:
            mid = (right+left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid
        return -1