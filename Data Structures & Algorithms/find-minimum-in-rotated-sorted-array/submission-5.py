class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        min_n = 1000

        if n == 1:
            return nums[0]
        if nums[l] < nums[r]:
            return nums[l]
        
        while l < r:
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] < nums[r]:
                min_n = min(min_n, nums[mid])
                r = mid
            if l == r:
                return nums[l]

        return min_n