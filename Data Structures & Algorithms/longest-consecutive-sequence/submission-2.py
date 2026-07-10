class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        num_set = set(nums)
        l = 1
        for n in num_set:
            if n-1 in num_set:
                continue
            else:
                while n+1 in num_set:
                    l += 1
                    n += 1
                max_length = max(max_length, l)
                l = 1
        return max_length

