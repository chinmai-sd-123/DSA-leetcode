class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

    # brute force solution where we use 3 loop - time complexity- o(n^3)
        # result=[]
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #                 if nums[i]+nums[j]+nums[k]==0:
        #                     triplet=[nums[i],nums[j],nums[k]]
        #                     triplet.sort()
        #                     if triplet not in result:
        #                         result.append(triplet)
                            
        # return result

    # optimal solution where we use two pointers - two sum+ fixed element - o(n^2)
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left< right:
                current_sum=nums[i]+nums[left]+nums[right]
                if current_sum==0:
                    triplet=[nums[i],nums[left],nums[right]]
                    result.append(triplet)
                    left+=1
                    right-=1

                    while left< right and nums[left]==nums[left-1]:
                        left+=1
                    while left< right and nums[right]==nums[right+1]:
                        right-=1
                elif current_sum>0:
                    right-=1
                else:
                    left+=1
        return result
                
