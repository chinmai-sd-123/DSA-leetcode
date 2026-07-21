class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
    #brute force time - o(n^2)

        # minimum= float('inf')
        
        # for i in range(len(nums)):
        #     sum=0
        #     for j in range(i,len(nums)):
        #         sum+=nums[i]
        #         if sum>= target:
        #             minimum=min(minimum,j-i+1)
        #             break
                    
        # if minimum==float('inf'):
        #     return 0
        # return minimum

    # sliding window - optimal - O(n) and space -O(1)

        l=0
        sum=0
        minimum=float('inf')
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>=target:
                minimum=min(minimum, r-l+1)
                sum-=nums[l]
                l+=1
    
        if minimum==float('inf'):
            return 0
        return minimum