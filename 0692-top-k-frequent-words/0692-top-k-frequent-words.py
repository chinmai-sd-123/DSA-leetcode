from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq=Counter(words) #counting the no. of freq of each string
        heap=[] # heap creation
        for key, value in freq.items(): #taking the string and freq and pushing into heap
            heapq.heappush(heap, (-value,key)) # the order comes from left to right(so if same freq , it takes alpahbetical order(tuple))
        ans=[]  # creation of empty list

        for i in range(k): # loop until k value
            item=heapq.heappop(heap) # pop the items we need
            ans.append(item[1]) # will add to list
        return ans # return list
        