class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    # brute force solution where time complexity is o(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False

    #using sorting helps bring duplicate adjacent then comparing them will give time complexity o(nlogn)
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True
        # return False

    #optimal solution where using set helps us getting time complexity o(n)
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False