class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # # for i in range(len(nums)):
        #     count=0
        #     for j in range(len(nums)):
        #         if nums[i]==nums[j]:
        #             count+=1
        #     if count==1:
        #         return nums[i]

        # from collections import Counter
        # count=Counter(nums)
        # for num in nums:
        #     if count[num]==1:
        #         return num
        # l=0
        # h=len(nums)-1
        # while l<=h:
        #     m=(l+h)//2
        
        # s= sum(nums)
        # set_s=set(nums)
        # s_2=sum(set_s)*2
        # return s_2-s

        result=0
        for num in nums:
            result^=num
        return result