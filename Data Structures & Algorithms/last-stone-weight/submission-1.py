class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        stones = [-i for i in stones]
        heapq.heapify(stones)

        while stones and len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)

            diff = abs(x - y)
            if diff:
                heapq.heappush(stones, -1 * diff)
        
        return -1 * stones[0] if stones else 0





        