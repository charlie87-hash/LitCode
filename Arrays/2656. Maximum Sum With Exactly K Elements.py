# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # Sort the nums list in ascending order
        nums.sort()
        score = 0
        while k > 0:
            # Find the larggest element in nums
            largest = nums.pop()
            score += largest

            # Increment the larggest element and add it back to nums
            nums.append(largest + 1)
            k -= 1

        return score