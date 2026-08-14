class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    # brute force - time- O(n * k)
    #     for _ in range(k):
    #         last=nums.pop()
    #         nums.insert(0,last)
        k=k%len(nums)
        nums.reverse()
        nums[:k]=nums[:k][::-1]
        nums[k:]=nums[k:][::-1]

