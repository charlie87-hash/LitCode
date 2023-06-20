# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        #iterate through nums
        #intiate i = 0 & j = 1, count = 0
        #get the absolute difference of nums[i] & nums[j]
        #return the counts

        i, j, count = 0, 1, 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count