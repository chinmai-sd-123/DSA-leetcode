class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
    # brute force solution with time complexity- o(n^2)
        # highest=0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         # if height[i]>=height[j]:
        #         #     volume=height[j]*(j-i)
        #         # elif height[i]<=height[j]:
        #         #     volume=height[i]*(j-i)
                # '''width=j-i
                #  container_height=min(height[i],height[j])
                #  volume=container_height*width'''
        #         highest=max(highest,volume)
        # return highest

    # time compexity - o(n)
        left=0
        right=len(height)-1
        highest=0
        while left <right:
            width=right-left
            container_height=min(height[left],height[right])
            area= container_height*width
            highest=max(highest,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return highest
                
