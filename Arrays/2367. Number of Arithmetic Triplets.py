# https://leetcode.com/problems/number-of-arithmetic-triplets/

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # Step 1: Count the frequency of each number in the input array
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Iterate over all triplets of indices (i, j, k) such that i < j < k
        result = 0
        for j in range(1, len(nums) - 1):
            i = j - 1
            k = j + 1
            while i >= 0 and k < len(nums):
                # Step 3: Check if nums[i], nums[j], and nums[k] form an arithmetic triplet
                if nums[j] - nums[i] == nums[k] - nums[j] == diff:
                    # Step 4: Add the number of arithmetic triplets that can be formed by nums[i], nums[j], and nums[k]
                    result += freq[nums[i]] * freq[nums[j]] * freq[nums[k]]
                    # Step 5: Move i and k to check for more arithmetic triplets
                    i -= 1
                    k += 1
                elif nums[k] - nums[j] < diff:
                    # Step 6: If nums[k] - nums[j] < diff, increase k to find a larger difference
                    k += 1
                else:
                    # Step 7: If nums[k] - nums[j] > diff, decrease i to find a smaller difference
                    i -= 1

        # Step 8: Return the total number of arithmetic triplets
        return result