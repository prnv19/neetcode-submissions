class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_len, length = 0, 0

        for num in nums:
            if num - 1 not in numset:
                length = 1
                
                while num + length in numset:
                    length += 1
                
                max_len = max(max_len, length)
        
        return max_len
            



        