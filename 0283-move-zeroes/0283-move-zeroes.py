class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count=0
        # while 0 in nums:
        #     nums.remove(0)
        #     count+=1
        # while count>0:
        #     nums.append(0)
        #     count-=1    

        l=0
        r=1
        while r<len(nums):
            if nums[l]==0 and nums[r]!=0:
                nums[l], nums[r]=nums[r],nums[l]
                l+=1
            elif nums[l]!=0:
                l+=1
            r+=1