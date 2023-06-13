# https://leetcode.com/problems/decode-xored-array/
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # get the first and push it to the output
        # get the xor of the values in the output and XOR with the encoded values
        # return output
        output = [first]

        for i in range(len(encoded)):
            output.append(output[-1] ^ encoded[i])
        return output
