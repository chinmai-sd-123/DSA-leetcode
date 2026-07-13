class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
    #hashmap + sorting time complexity - o(n+ m log m)
        # hashmap={}
        # for num in nums:
            
        #     hashmap[num]=hashmap.get(num,0)+1
            
        # sorted_items= sorted(hashmap.items(), key= lambda x:x[1],reverse=True)
        # result=[]

        # for num,freq in sorted_items[:k]:
        #     result.append(num)

        # return result
    
    # heap with time complexity- o(n log k)

        # import heapq
        # hashmap={}
        # heap=[]
        # for num in nums:
        #     hashmap[num]=hashmap.get(num,0)+1
        # for num, freq in hashmap.items():
        #     heapq.heappush(heap, (freq,num))
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        # result=[]
        # for freq, num in heap:

        #     result.append(num)
        # return result

    # bucket sort - time complexity o(n)

        hashmap={}
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        bucket= [[] for _ in range(len(nums)+1)]
        for num,freq in hashmap.items():
            bucket[freq].append(num)
        result=[]
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result)==k:
                    return result