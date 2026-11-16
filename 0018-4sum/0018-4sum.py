class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # result=set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             for l in range(k+1,len(nums)):
        #                 if nums[i]+nums[j]+nums[k]+nums[l]==target:
        #                     result.add(tuple(sorted([nums[i],nums[j],nums[k],nums[l]])))

        # return [list(x) for x in result]
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l=j+1
                r=len(nums)-1
                while l<r:
                    total= nums[i]+nums[j]+nums[l]+nums[r]
                    if total<target:
                        l+=1
                    elif target<total:
                        r-=1
                    else:
                        result.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
        return result

