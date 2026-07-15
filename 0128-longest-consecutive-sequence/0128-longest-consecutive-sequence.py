class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # brute force solution with time complexity - o(n^2)
        # max_len=0
        # for i in range(len(nums)):
        #     current=nums[i]
        #     length=1
        #     while current+1 in nums:
        #         current+=1
        #         length+=1
        #     max_len=max(max_len, length)
        # return max_len

    # optimal solution with time complexity - o(n)
    # bcz heree it does go check every chanin again and again
        num_set=set(nums)
        max_len=0
        for num in num_set:
            if num-1 not in num_set:
                current=1
                
                while num+current in num_set:
                    current+=1
                max_len=max(max_len, current)

        return max_len