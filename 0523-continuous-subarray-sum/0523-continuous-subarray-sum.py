class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
    # brute force sol- time complexity o- (n^2)
    #its not optimal
        # if not nums: return False
        # for i in range(len(nums)):
        #     sum=0
        #     for j in range(i,len(nums)):
        #         sum+=nums[j]
        #         if sum%k==0 and (j-i+1)>=2:
        #             return True

        # return False

        hashmap={0:-1}
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            remainder=prefix%k
            if remainder in hashmap:
                if i -hashmap[remainder]>=2:
                    return True
            else:
                hashmap[remainder]=i
        return False
        