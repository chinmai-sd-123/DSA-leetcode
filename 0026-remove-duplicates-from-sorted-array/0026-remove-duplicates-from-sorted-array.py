class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        # temp=[]
        # for num in nums:
        #     if num not in temp:
        #         temp.append(num)
        # k=len(temp)
        # for i in range(len(temp)):
        #     nums[i]=temp[i]
        # return k


        l=0
        for r in range(1,len(nums)):
            if nums[r]!=nums[l]:
                l+=1
                nums[l]=nums[r]
        return l+1