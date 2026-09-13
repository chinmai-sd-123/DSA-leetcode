class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # brute force - O(n^2)
        # max_area=0

        # for i in range(len(heights)):
        #     minimum=heights[i]
        #     for j in range(i,len(heights)):
        #         minimum=min(minimum,heights[j])
        #         area=minimum*(j-i+1)
        #         max_area=max(area,max_area)
        # return max_area

        # optimal sol - O(n)- monotonic stack
        maxArea= 0
        stack= [] # store in pair (index, height)
        for i, h in enumerate(heights):
            start= i
            while stack and stack[-1][1]> h:
                index, height= stack.pop()
                maxArea= max(maxArea, height*(i-index))
                start= index
            stack.append((start,h))

        for i , h in stack:
            maxArea= max(maxArea, h*(len(heights)-i))
        return maxArea