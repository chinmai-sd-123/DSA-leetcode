class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
    # brute force sol- O(n^2) space - O(1)
       
        # count=0
        # for i in range(len(nums)):
        #     sum=0
        #     for j in range(i,len(nums)):
        #         sum+=nums[j]
        #         if sum==k:
        #             count+=1
        # return count

    # optimal solution - prefix sum- time-o(n)
        hashmap={0:1}
        prefix=0
        count=0
        for num in nums:
            prefix+=num
            if prefix-k in hashmap:
                count+=hashmap[prefix-k]
            hashmap[prefix]=hashmap.get(prefix,0)+1
        
        return count