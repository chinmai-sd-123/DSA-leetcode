class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # result=[]
        # seen=set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 triplet=tuple(sorted([nums[i],nums[j],nums[k]]))
        #                 if triplet not in seen:
        #                     seen.add(triplet)
        #                     result.append(list(triplet))
        # return result
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                break
            l=i+1
            r=len(nums)-1
            while l< r:
                total=nums[i]+nums[l]+nums[r]
                if total<0:
                    l+=1
                elif total>0:
                    r-=1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return result