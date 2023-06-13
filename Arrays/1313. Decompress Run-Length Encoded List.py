# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # Initialize an empty list for the decompressed output
        decompressed = []
        # Get the length of the input list
        n = len(nums)
        # Loop through the input list, processing pairs of adjacent elements
        for i in range(0, n, 2):
            # Extract the frequency and value for the current pair
            freq, val = nums[i], nums[i+1]
            # Create a sublist of length freq consisting of the value val
            sublist = [val] * freq
            # Append the sublist to the decompressed output list
            decompressed.extend(sublist)
        # Return the decompressed output list
        return decompressed