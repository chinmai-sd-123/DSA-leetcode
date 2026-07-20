class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

    # brute force with time complexity-o(n) but space -O(n)
        # temp=[]

        # for num in nums:
        #     if num!=0:
        #         temp.append(num)
        
        # zeroes=len(nums)-len(temp)
        # while zeroes>0:
        #     temp.append(0)
        #     zeroes-=1
        # for i in range(len(nums)):
        #     nums[i]=temp[i]

        # return nums

    # optimal solution using two pointers - time -o(n) and space -O(1)
        left=0
        right=0
        while right<len(nums):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
            right+=1
            