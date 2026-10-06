class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l=0
        h=len(nums)-1
        first=-1
        last=-1
        while l<=h:
            m=(l+h)//2
            if nums[m]==target:
                first=m
                h=m-1
            elif nums[m]<target:
                l=m+1
            else:
                h=m-1
        l=0
        h=len(nums)-1
        while l<=h:
            m=(l+h)//2
            if nums[m]==target:
                last=m
                l=m+1
            elif nums[m]<target:
                l=m+1
            else:
                h=m-1
        return [first, last]
