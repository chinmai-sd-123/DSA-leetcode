import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap=[]
        for point in points:
            dist=point[0]**2 + point[1]**2
            heapq.heappush(heap, (-dist,point))
            if len(heap)>k:
                heapq.heappop(heap)
        return [x[1] for x in heap]
            