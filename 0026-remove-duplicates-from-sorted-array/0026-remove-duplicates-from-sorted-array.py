class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

    # brute force solution with time - o(n) and space o(n)
        # temp=[]
        # for num in nums:
        #     if num not in temp:
        #         temp.append(num)

        # k=len(temp)
        # for i in range(len(temp)):
        #     nums[i]=temp[i]

        # return k
    # optimal sol with time - o(n) and space - o(1)
        if len(nums)==0:
            return 0
        left=0 
        for right in range(1, len(nums)):
            if nums[left]!=nums[right]:
                left+=1
                nums[left]=nums[right]
        return left+1
        