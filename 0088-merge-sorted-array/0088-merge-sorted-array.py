class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # brute force solution where we first copy numbers from nums2 to nums1 replacing zero then sorting nums1
        for i in range(n):
            nums1[m+i]=nums2[i]

        for i in range(len(nums1)):
            for j in range(i+1,len(nums1)):
                if nums1[i]>nums1[j]:
                    nums1[i], nums1[j]=nums1[j], nums1[i]
        return nums1
