class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        output = [1]*size

        prefix = 1
        for i in range(size):
            output[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(size-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output