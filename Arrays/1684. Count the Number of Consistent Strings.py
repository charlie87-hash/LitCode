# https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_chars = set(allowed)
        count = 0
        for word in words:
            if set(word).issubset(allowed_chars):
                count += 1
        return count