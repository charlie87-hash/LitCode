# https://leetcode.com/problems/left-and-right-sum-differences/description/

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n
        answer = [0] * n

        # Calculate left sum for each index
        for i in range(1, n):
            left_sum[i] = left_sum[i-1] + nums[i-1]

        # Calculate right sum for each index
        for i in range(n-2, -1, -1):
            right_sum[i] = right_sum[i+1] + nums[i+1]

        # Calculate answer for each index
        for i in range(n):
            answer[i] = abs(left_sum[i] - right_sum[i])

        return answer