class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for i,num in enumerate(nums):
            c = target- num
            if c in hashmap:
                return [i,hashmap[c]]
            hashmap[num]=i