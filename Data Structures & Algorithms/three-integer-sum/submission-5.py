class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            
            if i > 0 and nums[i - 1] == a:
                continue

            l,r = i+1, len(nums) - 1

            while l < r:
                # print(f"{a}. {nums[l]} {nums[r]}")
                if a + nums[l] + nums[r] == 0:
                    if [a, nums[l], nums[r]] not in res:
                        res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                if a + nums[l] + nums[r] > 0:
                    r -= 1
                if a + nums[l] + nums[r] < 0:
                    l += 1
        return res
                
 
        