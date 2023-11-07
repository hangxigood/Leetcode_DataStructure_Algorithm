class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        elif len(cost) == 3:
            return min(cost[1], cost[0]+cost[2])
        else:
            return min(self.minCost(cost, 0), self.minCost(cost, 1))
    
    def minCost(self, cost, i):
        pay = cost[i]
        while i<= len(cost) - 3:
            if cost[i+1] >= cost[i+2]:
                pay += cost[i+2]
                i += 2
            else:
                pay += cost[i+1]
                i += 1
        return pay