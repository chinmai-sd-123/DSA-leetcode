class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

    # brute force solution with time complexity - o(n^2)
        # for i in range(len(nums)):
        #     count=0
        #     for j in range(len(nums)):
        #         if nums[i]==nums[j]:
        #             count+=1
        #     if count>=len(nums)/2:
        #         return nums[i]

    #optimal using hashmap with time complexity- o(n)

        # hashmap={}
        # for num in nums:
        #     hashmap[num]=hashmap.get(num,0)+1

        # for key,value in hashmap.items():
        #     if value>len(nums)//2:
        #         return key
    
    #now wht if we try getting time complexity-o(n) but space o(1) using special algo
    # boyer moore voting
        count=0
        for num in nums:
            if count ==0:
                candidate=num
            if candidate==num:
                count+=1
            else:
                count-=1
        return candidate

