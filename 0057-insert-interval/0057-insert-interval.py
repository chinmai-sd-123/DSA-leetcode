class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result=[]
        for i , interval in enumerate(intervals):
            if interval[1]<newInterval[0]:
                result.append(interval)
            elif interval[0]<= newInterval[1]:
                newInterval[0]=min(interval[0],newInterval[0])
                newInterval[1]=max(interval[1],newInterval[1])

            else:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
        result.append(newInterval)
        return result