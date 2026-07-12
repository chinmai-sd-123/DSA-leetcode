class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap={}
        for num in nums:
            
            hashmap[num]=hashmap.get(num,0)+1
            
        sorted_items= sorted(hashmap.items(), key= lambda x:x[1],reverse=True)
        result=[]

        for num,freq in sorted_items[:k]:
            result.append(num)

        return result
