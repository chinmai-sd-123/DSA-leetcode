class Solution(object):
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # for row in matrix:
        #     if target<=row[-1]:
        #         low=0
        #         high=len(row)-1
        #         while low<=high:
        #             mid=(low+high)//2
        #             if row[mid]==target:
        #                 return True
        #             elif target>row[mid]:
        #                 low=mid+1
        #             else :high=mid-1
        #         return False
        # return False

        low=0
        high=(len(matrix)*len(matrix[0])-1)
       
        while low<=high:
            mid=(low+high)//2
            x=matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            if x==target:
                return True
            elif target>x:
                low=mid+1
            else:
                high=mid-1
        return False
                



