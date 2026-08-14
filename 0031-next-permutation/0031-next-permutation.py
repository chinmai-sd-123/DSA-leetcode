class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    # optimal - O(n) and space -O(1)
        #find pivot from right
        pivot=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                pivot=i
                break

        if pivot==-1:
            nums.reverse()
            return
        #search for next greater than pivot
        j=len(nums)-1
        while nums[j]<=nums[pivot]:
            j-=1
        # swap
        nums[pivot], nums[j]= nums[j], nums[pivot]
        # reverse suffix of pivot
        # nums[pivot+1:]=nums[pivot+1:][::-1]
        
        l=pivot+1
        r=len(nums)-1
        while l<r:
            nums[l], nums[r]=nums[r],nums[l]
            l+=1
            r-=1
      
