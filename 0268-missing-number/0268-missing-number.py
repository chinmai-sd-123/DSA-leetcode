class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

    # brute force solujtion with time complexity- o(n^2)

        # for i in range(len(nums)+1): - o(n)
        #     if i not in nums: here - o(n)
        #         return i
    # better solution using hashset- o(n)
        # num_set=set(nums)
        # for i in range(len(nums)+1):
        #     if i not in num_set: 
        #         return i

    #mathematical solution- o(n)
        # return len(nums)*((len(nums)+1))//2-sum(nums)

    # xor sol- o(n) with space o(1)

        xor=0
        for i in range(len(nums)+1):
            xor^=i
        for num in nums:
            xor^=num
        return xor