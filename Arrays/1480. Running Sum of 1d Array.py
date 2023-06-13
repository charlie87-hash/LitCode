# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #create a list of output
        #add the first value of nums[0] to it
        #put the result of the sum to the output
        output = []
        res = 0
        for i in nums:
            res = i + res
            output.append(res)
        return output