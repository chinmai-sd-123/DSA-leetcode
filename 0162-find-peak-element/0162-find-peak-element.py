class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        for i in range(1,n-1):          
            if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                return i
        return n-1