class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    #brute force solution with time complexity - o(n^2)
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]>nums[j]:
        #             nums[i],nums[j]=nums[j],nums[i]
        # return nums

    #better solution with time complexity -o(n)
        # index=0
        # zero=one=two=0
        # for num in nums:
        #     if num==0:
        #         zero+=1
        #     elif num==1:
        #         one+=1
        #     else:
        #         two+=1
     
        # while zero >0:
        #     nums[index]=0
        #     index+=1
        #     zero-=1
        # while one >0:
        #     nums[index]=1
        #     index+=1
        #     one-=1
        # while two >0:
        #     nums[index]=2
        #     index+=1
        #     two-=1

        # return nums

    #better solution with time complexity - o(n)
        result=[]
        for i in range(3):
            count=0
            for num in nums:
                if num==i:
                    count+=1
            while count>0:
                result.append(i)
                count-=1
        nums[:]=result
        return nums