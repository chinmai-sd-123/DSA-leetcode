class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i]+numbers[j]==target:
        #             return [i+1,j+1]
    # will use two pointers whihc gives us time complexity o(n) with space O(1)
        left = 0
        right= len(numbers)-1

        while left < right:
            current_sum=numbers[left]+numbers[right]
            if current_sum==target:
                return[left+1,right+1]
            elif current_sum> target:
                right-=1

            else :
                left+=1 
            