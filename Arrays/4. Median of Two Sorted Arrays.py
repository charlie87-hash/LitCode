# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Combine the two arrays and sort them
        nums = nums1 + nums2
        nums.sort()

        # Calculate the index of the middle element
        mid = len(nums) // 2

        # If there are an odd number of elements, return the middle element
        if len(nums) % 2 != 0:
            return nums[mid]

        # If there are an even number of elements, calculate the average of the two middle elements
        # by summing the two middle elements and dividing by 2
        else:
            return (nums[mid - 1] + nums[mid]) / 2.0