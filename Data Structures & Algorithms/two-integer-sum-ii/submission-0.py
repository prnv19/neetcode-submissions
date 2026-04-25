class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for num in numbers:
            if target - num in numbers:
                return [numbers.index(num) + 1, numbers.index(target - num) + 1]
        