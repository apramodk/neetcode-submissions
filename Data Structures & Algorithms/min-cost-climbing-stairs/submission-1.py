class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # problem baseline
        # ok so from each index i in cost, we have to pay a cost defined in cost[i]
        # when we pay the cost[i] we can either step i+2 or i+1

        # 2 <= len(cost) <= 100
        # 0 <= cost[i] <= 100

        # we basically want to take the cheapest cost path to i = len(cost)
        minCost = 2**32
        # arr = [1,2,3]
        # mincostAti = [3,2,3]

        # cost =   [1,2,1,2,1,1,1]
        # mCostI = [4,5,3,3,2,1,1]
        # we could find the minimum cost at each index from the last element -> first element
        a,b = 0,0
        for c in cost[::-1]:
            a,b = c + min(a,b), a
            
        return min(a,b)