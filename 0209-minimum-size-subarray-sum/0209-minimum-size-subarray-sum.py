class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # minimum=float('inf')
        # for i in range(len(nums)):
        #     sums=0
        #     for j in range(i,len(nums)):
        #         sums+=nums[j]
        #         if sums>=target:
        #             minimum=min(minimum,j-i+1)
                    
        # return 0 if minimum==float('inf') else minimum
        l=0
        minimum= float('inf')
        total=0
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                minimum=min(minimum, r-l+1)
                total-=nums[l]
                l+=1
        return 0 if minimum == float('inf') else minimum