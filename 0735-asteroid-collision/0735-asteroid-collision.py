class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # brute force - O(n^2)
        # result=[]
        # for num in asteroids:
        #     result.append(num)
        #     while len(result)>=2 and result[-2]>0 and result[-1]<0:
        #         left=result[-2]
        #         right=result[-1]
        #         if abs(left)>abs(right):
        #             result.pop()
        #         elif abs(left)==abs(right):
        #             result.pop()
        #             result.pop()
        #         else:    
        #             result.pop(-2)
                    
        # return result

        # optimal solution - O(n)
        stack=[]
        for a in asteroids:
            while stack and stack[-1]>0 and a <0:
                if stack[-1] < - a:
                    stack.pop()
                    continue
                if stack[-1]==-a:
                    stack.pop()
                a=0
                break
            if a:
                stack.append(a)
        return stack
