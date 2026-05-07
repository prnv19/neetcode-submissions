class Solution:
    def trap(self, height: List[int]) -> int:
        # max_left = [-1] * len(height)
        # max_right = [-1] * len(height)

        # curr_left_max = -1
        # curr_right_max = -1
    
        # max_left[0] = 0
        # max_right[len(height) - 1] = 0

        # for i in range(1, len(height)):
        #     if height[i] > curr_left_max:
        #         curr_left_max = height[i]
        #         max_left[i] = curr_left_max
        #     else:
        #         max_left[i] = curr_left_max
            

        #     if height[len(height) - i - 1] > curr_right_max:
        #         curr_right_max = height[len(height) - i - 1]
        #         max_right[len(height) - i - 1] = curr_right_max
        #     else:
        #         max_right[len(height) - i - 1] = curr_right_max

        l, r = 0, len(height) - 1
        max_L, max_R = height[l], height[r]
        res = 0

        while l < r:
            if max_L < max_R:
                l += 1
                max_L = max(max_L, height[l])
                res += max_L - height[l]
            else:
                r -= 1
                max_R = max(max_R, height[r])
                res += max_R - height[r]
        
        return res
            







       