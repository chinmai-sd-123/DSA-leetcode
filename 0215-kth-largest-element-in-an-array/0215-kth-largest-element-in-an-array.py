import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # heapq.heapify(nums)
        # for _ in range(len(nums)-k):
        #     heapq.heappop(nums)
        # return nums[0]
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
            
        return heap[0]