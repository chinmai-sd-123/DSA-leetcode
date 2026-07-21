class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

    # brute force - time - O(n^2) space- o(n)
        # max_len=0
        # for i in range(len(nums)):
        #     count=0
        #     for j in range(i,len(nums)):
        #         if nums[j]==0:
        #             count+=1
        #         if count>k:
        #             break
        #         max_len=max(max_len,j-i+1)
        # return max_len
        
    # sliding window - optimal - time -O(n) and space- O(1)
        l=0
        count=0
        max_len=0
        for r in range(len(nums)):
            if nums[r]==0:
                count+=1
            while count >k:
                if nums[l]==0:
                    count-=1
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len