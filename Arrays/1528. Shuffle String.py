
# https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)                  # Get the length of the input string
        shuffled = [''] * n         # Initialize an empty list of the same length as the input string
        for i in range(n):          # Iterate over each index in the indices array
            shuffled[indices[i]] = s[i]  # Add the character at the current index in the input string to the corresponding
    # Join the characters in the shuffled list into a single string and return it
        return ''.join(shuffled)