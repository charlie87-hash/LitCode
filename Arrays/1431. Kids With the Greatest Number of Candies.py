# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # find the maxmum number of candies
        max_candies = max(candies)

        # initialize the boolean array of result

        result = [False] * len(candies)

        # check if each kid can have the greatest number of candies after receiveing the extra candies

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                result[i] = True

        return result