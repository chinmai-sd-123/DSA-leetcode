# from functools import lru_cache
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # intervals.sort(key= lambda x: x[0])
        # @lru_cache(None)
        # def solve(i, prev):
        #     if i==len(intervals):
        #         return 0
        #     remove=1+solve(i+1, prev)
        #     if prev==-1 or intervals[i][0]>=intervals[prev][1]:
        #         keep=solve(i+1,i)
        #         return min(keep, remove)
        #     return remove
        # return solve(0,-1)

        #greedy appraoch
        if not intervals:
            return 0
        intervals.sort(key= lambda x: x[1])
        removals= 0
        prev_end= intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0]<prev_end:
                removals+=1
            else:
                prev_end=intervals[i][1]
        return removals
            