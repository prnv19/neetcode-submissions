class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        counts = {}
        res = []
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for n, c in counts.items():
            freq[c].append(n)
        
        for i in range(len(freq) - 1, -1, -1):
            while freq[i]:
                res.append(freq[i].pop())
                k -= 1
                if k == 0:
                    return res
