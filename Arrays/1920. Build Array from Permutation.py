# https://leetcode.com/problems/build-array-from-permutation/

# perms = n!
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        ans = []

        #iterate through nums
        for i in range(len(nums)):
            #get the number at a given index
            ans.append(nums[nums[i]])
        return ans