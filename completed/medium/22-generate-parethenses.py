class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def backtrack(openN, closedN):
            # if we have hit the final combination of parentheses
            # return the stack
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # if we still haven't opened the max number of pthes
            if openN < n:
                # open another
                stack.append("(")
                # recursively call, and add one to the closed counter
                backtrack(openN + 1, closedN)
                # pop off the stack to close the rest of the pthes
                stack.pop()

            # if the number of closed pthes is less than the open ones, we have work to do
            if closedN < openN:
                # close a pair
                stack.append(")")
                # recursive call with one more closed
                backtrack(openN, closedN + 1)
                # pop off stack to remove this pair
                stack.pop()

        backtrack(0, 0)
        return res
            


            