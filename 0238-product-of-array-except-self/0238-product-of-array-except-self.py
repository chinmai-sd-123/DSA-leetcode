class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    # brute force solution with time complexuty - o(n^2)
        # result=[]
        # for i in range(len(nums)):
        #     product=1
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         product*=nums[j]
        #     result.append(product)
        # return result
    
    # optimal sdolution with time complexity - o(n)

        n=len(nums)
        right=[1]*n
        answer=[1]*n

        for i in range(1,n):
            answer[i]=answer[i-1]*nums[i-1]
        # for i in range(n-2,-1,-1):
        #     right[i]=right[i+1]*nums[i+1]
        #     answer[i]*=right[i]
        suffix=1
        for i in range(n-1,-1,-1):
            answer[i]*=suffix
            suffix*=nums[i]
        
        return answer