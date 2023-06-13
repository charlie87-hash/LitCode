# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            _count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    _count += 1
            output.append(_count)
        return output