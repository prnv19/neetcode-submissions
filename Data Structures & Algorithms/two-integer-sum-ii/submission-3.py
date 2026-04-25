class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # for num in numbers:
        #     if target - num in numbers:
        #         return [numbers.index(num) + 1, numbers.index(target - num) + 1]

        f, l = 0, len(numbers) - 1
        while f < l:
            curr_sum = numbers[f] + numbers[l]
            if curr_sum > target:
                l -= 1
            if curr_sum < target:
                f += 1
            if curr_sum == target:
                return [f+1, l+1]        