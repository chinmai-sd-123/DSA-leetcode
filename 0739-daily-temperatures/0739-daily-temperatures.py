class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # brute force - o(n^2)
        # array=[]
        # for i in range(len(temperatures)):
        #     count=0
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[i]<temperatures[j]:
        #             count=j-i
        #             break
        #     array.append(count)
                
        # return array

        res= [0]* len(temperatures)
        stack=[] # pair [temp, index]

        for i ,t in enumerate(temperatures):
            while stack and t> stack[-1][0]:
                stacktemp, stackind= stack.pop()
                res[stackind]= i-stackind
            stack.append([t,i])
        return res