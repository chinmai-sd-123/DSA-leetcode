class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
    # brute force - O(m*n)
        # zero_rows=[]
        # zero_columns=[]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]==0:
        #             zero_rows.append(i)
        #             zero_columns.append(j)
        
        # for row in zero_rows:
        #     for i in range(len(matrix[0])):
        #         matrix[row][i]=0

        # for column in zero_columns:
        #     for j in range(len(matrix)):
        #         matrix[j][column]=0
    
    # optimal -space -O(1)

        first_row_zero= False
        first_column_zero= False

        for i in range(len(matrix[0])):
            if matrix[0][i]==0:
                first_row_zero= True
        for j in range(len(matrix)):
            if matrix[j][0]==0:
                first_column_zero= True

        for i in range(1,len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        for i in range(1,len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j] ==0:
                    matrix[i][j]=0
        if first_row_zero: 
            for j in range(len(matrix[0])):
                matrix[0][j]=0
        if first_column_zero:
            for i in range(len(matrix)):
                matrix[i][0]=0