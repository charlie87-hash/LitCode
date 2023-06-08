# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        increments = "++X"
        increments1 = "X++"
        decrements = "--X"
        decrements1  = "X--"
        x = 0
        # iterate through the operations
        for operation in operations:
            if operation == increments or operation == increments1:
                x += 1
            else:
                if operation == decrements or operation == decrements1:
                    x -= 1
        return x