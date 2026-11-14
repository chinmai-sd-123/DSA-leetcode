class Solution:
    def trap(self, height: list[int]) -> int:
        # count=0
        # for i in range(len(height)):
        #     max_l= max(height[:i+1])
        #     max_r= max(height[i:])
        #     water=min(max_l,max_r)-height[i]
        #     count+=water
        # return count

        l, r, l_max, r_max,total = 0, len(height)-1, 0, 0 , 0
        while l<r:
            if height[l]<height[r]:
                l_max=max(l_max, height[l])
                total+=l_max-height[l]
                l+=1
            else:
                r_max=max(r_max, height[r])
                total+=r_max-height[r]
                r-=1
        return total