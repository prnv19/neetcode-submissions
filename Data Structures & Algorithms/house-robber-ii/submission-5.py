class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_houses(hosues):
            dp = [0 for _ in range(len(hosues) + 2)]
            for i in range(len(hosues) - 1, -1, -1):
                dp[i] = max(hosues[i] + dp[i + 2], dp[i + 1])
            return dp[0]
        return max(rob_houses(nums[1:]), rob_houses(nums[:-1]))

        