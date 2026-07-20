class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
    #brute force timw- o(n^2) and space- O(n)
        # total=0
        # for i in range(len(height)):
        #     leftMax=0
        #     rightMax=0

        #     for j in range(i+1):
        #         leftMax=max(leftMax, height[j])
        #     for j in range(i,len(height)):
        #         rightMax=max(rightMax, height[j])

        #     water= min(rightMax, leftMax)-height[i]
        #     total+=water
        # return total

    # optimal sol - space - O(1)

        if not height: return 0
        total=0
        l,r = 0, len(height)-1
        leftMax,rightMax= height[l], height[r]

        while l<r:  
            if leftMax < rightMax:
                l+=1
                leftMax=max(leftMax, height[l])
                total+=leftMax- height[l]

            else:
                r-=1
                rightMax=max(rightMax, height[r])
                total+=rightMax- height[r]
        return total

    