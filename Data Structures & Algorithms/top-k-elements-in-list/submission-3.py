class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for c in count:
            freq[count[c]].append(c)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            # if len(freq) > 0:
            for f in freq[i]:
                res.append(f)
                if len(res) == k:
                    return res



        