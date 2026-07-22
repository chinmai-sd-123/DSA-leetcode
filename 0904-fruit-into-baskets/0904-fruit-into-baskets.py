class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
    # brute force solution - time complexity- O(n^2)

        # hashmap={}
        # max_len=0
        # for i in range(len(fruits)):
        #     hashmap={}
        #     for j in range(i,len(fruits)):
        #         hashmap[fruits[j]]=hashmap.get(fruits[j],0)+1
        #         if len(hashmap)>2:
        #             break
        #         max_len=max(max_len,j-i+1)

        # return max_len

    # optimal sol - o(n) and space- O(k)
        l=0
        hashmap={}
        max_len=0
        for r in range(len(fruits)):
            hashmap[fruits[r]]=hashmap.get(fruits[r],0)+1

            while len(hashmap)>2: 
                hashmap[fruits[l]]-=1
                if hashmap[fruits[l]]==0:   
                    del hashmap[fruits[l]]
                
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len
                
                
                