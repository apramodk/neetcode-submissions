class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # given a list of stones, we want to grab the 2 heaviest stones
        # represented as x,y
        # if x == y, both stones are destroyed
        # otherwise, the lighter stone is destroyed
        # we want to basically keep returning this until we are left with at most 1 stone

        stones = [stone*-1 for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            # if they equal, dont push back in
            if x != y:
                heapq.heappush(stones, -abs(x-y))

        return 0 if len(stones) == 0 else stones[0]*-1