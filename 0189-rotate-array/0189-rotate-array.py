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
    # optimal using reverse - O(n)
        # k=k%len(nums)
        # nums.reverse()
        # nums[:k]=nums[:k][::-1]
        # nums[k:]=nums[k:][::-1]

    # optimal - O(n) spze- O(1)

        def reverse(left, right):
            while left < right:
                nums[left], nums[right]= nums[right], nums[left]
                left+=1
                right-=1

        k=k%len(nums)
        reverse(0, len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)
