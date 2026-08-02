class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        pivot = l

        def binary_search(l: int, r: int) -> int:
            while l <= r:
                mid = (l+r)//2
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        res = binary_search(0, pivot-1)
        return res if res != -1 else binary_search(pivot, n-1)