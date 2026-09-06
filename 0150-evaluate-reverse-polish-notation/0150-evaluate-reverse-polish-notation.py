class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        # time O(n)
        stack=[]
        for ch in tokens:

            if ch in "+-*/":
                first=stack[-1]
                stack.pop()
                second=stack[-1]
                stack.pop()
                if ch == "+":
                    operation=second+first
                elif ch == "-":
                    operation= second- first
                elif ch == "*":
                    operation=second*first
                else:
                    operation = abs(second) // abs(first) # truncate toward zero
                    if (second < 0) != (first < 0):
                        operation = -operation
                stack.append(operation)
            else:
                cha=int(ch)
                stack.append(cha)
        return stack[-1] 