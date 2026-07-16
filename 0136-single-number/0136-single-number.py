class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

    # brute force solution with time complexity- o(n^2)
        # for i in range(len(nums)):
        #     count=0
        #     for j in range(len(nums)):
        #         if nums[i]==nums[j]:
        #             count+=1
        #     if count==1:
        #         return nums[i]

    # better solution using hashmap with time complexity - o(n)

        # hashmap={}
        # for num in nums:
        #     hashmap[num]=hashmap.get(num,0)+1
        # for key,value in hashmap.items():
        #     if value==1:
        #         return key
    # using xor will get time complexity- o(n) with space -o(1)
        xor=0
        for num in nums:
            xor^=num
        return xor