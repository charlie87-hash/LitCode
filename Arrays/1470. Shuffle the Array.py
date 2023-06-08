# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # divide the array by n into 2

        # first array x- i
        # second array y -j
        # add both arrays based of indexes, x first and y last
        output = []

        for i in range(n):
            output.append(nums[i])

            output.append(nums[i + n])

        return output


"""
def rearrange_array(nums):
    x = nums[:n]  # Split the array nums into the first half (x) up to index n
    y = nums[n:]  # Split the array nums into the second half (y) starting from index n
    result = []  # Initialize an empty array to store the rearranged elements
    for i in range(n):
        result.append(x[i])  # Append the ith element of x to the result array
        result.append(y[i])  # Append the ith element of y to the result array
    return result  # Return the final rearranged array

"""