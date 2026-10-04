import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # minimum=float('inf')
        # for k in range(1, max(piles)+1):
        #     hours=0
        #     for i in range(len(piles)):
        #         hours+=math.ceil(piles[i]/k)
        #     if hours<=h:
        #         minimum=min(minimum,k)
        # return minimum 

        low=1
        high=max(piles)
        while low<=high:
            mid=(low+high)//2
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/mid)
            if hours<=h:
                high=mid-1
            else:
                low=mid+1
        return low
            


