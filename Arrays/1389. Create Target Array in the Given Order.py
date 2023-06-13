# https://leetcode.com/problems/create-target-array-in-the-given-order/
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # Create an empty list to store the target array
        target = []
        # Iterate over the elements in nums and index lists
        for i in range(len(nums)):
            # Insert the element from nums at the specified index in the target list
            target.insert(index[i], nums[i])

        # Return the target array
        return target
