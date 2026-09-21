class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            if n + 1 in nums:
                continue
            
            length = 1
            while n - 1 in nums:
                n = n - 1
                length += 1
            res = max(res, length)
        
        return res
