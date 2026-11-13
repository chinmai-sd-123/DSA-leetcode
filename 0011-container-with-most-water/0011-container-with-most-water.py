class Solution:
    def maxArea(self, height: list[int]) -> int:
        # max_area=0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         area=min(height[i],height[j])*(j-i)
        #         max_area=max(max_area,area)
        # return max_area
                
        l=0
        r=len(height)-1
        max_area=0
        while l<r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
            
