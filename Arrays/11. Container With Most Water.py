# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0  # initialize left pointer to the beginning of the array
        right = len(height) - 1  # initialize right pointer to the end of the array
        max_area = 0  # initialize the maximum area to 0

        while left < right:  # continue until left pointer is less than right pointer
            # calculate the area of the container with the current pointers
            area = min(height[left], height[right]) * (right - left)

            # update the maximum area if the current area is greater
            max_area = max(max_area, area)

            # move the pointer that points to the shorter wall
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area  # return the maximum area
