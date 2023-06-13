# https://leetcode.com/problems/min-cost-climbing-stairs/


# use recursion

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Create a memory to store the computed minimum costs
        mem = {}

        def minCost(i):
            # Check if the minimum cost for the current step has already been computed
            if i in mem:
                return mem[i]

            # Base case: if the current step is 0 or 1, return the cost of that step
            if i <= 1:
                return cost[i]

            # Recursive case: calculate the cost of reaching the current step
            # by adding the cost of the current step to the minimum cost of
            # reaching the previous two steps
            result = cost[i] + min(minCost(i - 1), minCost(i - 2))

            # Store the computed min cost in the mem
            mem[i] = result

            return result

        # Get the total number of steps
        n = len(cost)

        # Return the min cost of reaching the last step or 2nd last step
        # by calling the recursive function minCost
        return min(minCost(n - 1), minCost(n - 2))
