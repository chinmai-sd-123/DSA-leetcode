class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # brute force solution with time complexity- o(n^2)
        # for i in range(len(nums)):
        #     count=0
        #     for j in range(len(nums)):
        #          if nums[i]==nums[j]:
        #             count+=1
        #     if count>1:
        #         return nums[i]

    # better solution using hashmap with time complexity - o(n)
        # hashmap={}
        # for num in nums:
        #     hashmap[num]=hashmap.get(num,0)+1
        # for key, value in hashmap.items():
        #     if value>1:
        #         return key

    # optimal solution with time complexity - o(n) and space complexity- o(1)

    # using floyd's cycle detection with two pointers
        slow=0
        fast=0

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]        
            if slow==fast:
                break
        slow=0
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow