class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

    # brute force - time- O(n^2)
        # maximum=float("-inf")
        # for i in range(len(nums)):
        #     sum=0
        #     for j in range(i,len(nums)):
        #         sum+=nums[j]
        #         maximum=max(maximum,sum)
        # return maximum

    #kadens algo- time O(n) and space -O(1)
        current=0
        maximum= float("-inf")
        for num in nums:
            current+=num
            maximum=max(maximum,current)
            if current<0:
                current=0
        return maximum