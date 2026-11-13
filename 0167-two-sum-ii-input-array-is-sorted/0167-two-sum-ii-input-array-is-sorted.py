class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i]+numbers[j]==target:
        #             return [i+1,j+1]

        l, r= 0, len(numbers)-1
        while l<r:
            current_sum=numbers[l]+numbers[r]
            if target> current_sum:
                l+=1
                continue
            elif target<current_sum:
                r-=1
                continue
            else:
                return [l+1,r+1]
        return []