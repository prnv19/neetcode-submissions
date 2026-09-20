class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]
        postfix = [1 for _ in range(len(nums))]
        
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i - 1]
            prefix[i] = prod
        
        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            postfix[i] = prod
        
        return [i*j for i,j in zip(prefix, postfix)]

        