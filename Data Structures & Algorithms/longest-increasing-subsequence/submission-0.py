class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [0] * len(nums)
        maxlen = -1

        for i in range(len(LIS) - 1, -1, -1):
            LIS[i] = 1
            for j in range(i, len(LIS)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
            
            maxlen = max(maxlen, LIS[i])
        return maxlen
                

        