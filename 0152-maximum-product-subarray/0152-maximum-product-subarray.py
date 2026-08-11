class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # brute force - time O(n^2)
        # maximum=float('-inf')
        # for i in range(len(nums)):
        #     product=1
        #     for j in range(i,len(nums)):
        #         product*=nums[j]
        #         maximum=max(maximum,product)
        # return maximum

    #optimal solution - O(n)
        current_max= nums[0]
        current_min= nums[0]
        maximum= nums[0]
        for i in range(1,len(nums)):
            new_max = max(nums[i], nums[i] * current_max, nums[i] * current_min)
            new_min = min(nums[i], nums[i] * current_max, nums[i] * current_min)
            current_max=new_max
            current_min=new_min
            maximum=max(maximum, current_max)
        return maximum
            