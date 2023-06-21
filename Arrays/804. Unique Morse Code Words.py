# https://leetcode.com/problems/unique-morse-code-words/
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Define the Morse code dictionary
        morse_code_dict = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
            'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
            'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
            'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
            'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
            'z': '--..'
        }

        # Use a set to keep track of unique transformations
        transformations = set()

        # Iterate over each word and generate its Morse code transformation
        for word in words:
            transformation = ""
            for char in word:
                transformation += morse_code_dict[char]
            transformations.add(transformation)

        # Return the number of unique transformations
        return len(transformations)