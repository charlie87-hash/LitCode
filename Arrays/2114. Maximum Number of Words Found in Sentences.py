# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # Initialize a variable to store the maximum number of words
        max_words = 0

        # Iterate through each sentence in the array
        for sentence in sentences:
            # Split the sentence into words using the split() method
            words = sentence.split()

            # Update the maximum number of words if necessary
            if len(words) > max_words:
                max_words = len(words)

        return max_words