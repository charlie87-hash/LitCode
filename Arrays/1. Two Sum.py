# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty list to store the output indices
        output = []

        # Loop through each element in the nums list
        for i in range(len(nums)):
            # Loop through each subsequent element in the nums list
            for j in range(i + 1, len(nums)):
                # Check if the sum of the current element and the subsequent element is equal to the target
                if nums[i] + nums[j] == target:
                    # If it is, append the indices of the two elements to the output list
                    # output.append(i)
                    # output.append(j)
                    output += [i, j]

        # Return the output list containing the indices of the two numbers that add up to the target value
        return output