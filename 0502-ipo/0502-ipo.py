class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        min_heap=[]
        max_heap=[]
        for i in range(len(profits)):
            heapq.heappush(min_heap, (capital[i],profits[i]))
        for _ in range(k):
            while min_heap and w >= min_heap[0][0]:               
                affordable=heapq.heappop(min_heap)
                heapq.heappush(max_heap,-affordable[1])
            if not max_heap:break
            w+= -heapq.heappop(max_heap)
        return w
