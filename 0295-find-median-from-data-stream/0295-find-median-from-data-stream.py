import heapq
class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        x=-heapq.heappop(self.small)
        heapq.heappush(self.large, x)
        if len(self.large)>len(self.small):
            y=-heapq.heappop(self.large)
            heapq.heappush(self.small, y)


    def findMedian(self) -> float:
        if len(self.small)==len(self.large):
            return (-self.small[0]+self.large[0])/2
        else:
            return -self.small[0]
    
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()