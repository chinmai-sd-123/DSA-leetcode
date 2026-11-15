class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # num=[]
        # for i in range(len(nums)):
        #     num.append(pow(nums[i],2))
        # num.sort()
        # return num
        pos=len(nums)-1
        array=[0]*len(nums)
        l, r= 0, len(nums)-1
        while l<=r:
            if abs(nums[l])<abs(nums[r]):
                array[pos]=nums[r]**2
                r-=1
                pos-=1
            else:
                array[pos]=nums[l]**2
                l+=1
                pos-=1

        return array