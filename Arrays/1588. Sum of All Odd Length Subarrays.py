# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)  # length of the input array
        res = 0  # initialize the result variable to zero
        # loop over all possible odd lengths of subarrays
        for i in range(n):
            for j in range(i + 1, n + 1):
                if (j-i) % 2 == 1:
                    res += sum(arr[i:j])
        return res