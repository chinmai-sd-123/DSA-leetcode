class TimeMap:

    # def __init__(self):
    #     self.store={}

    # def set(self, key: str, value: str, timestamp: int) -> None:
    #     if key not in self.store:
    #         self.store[key]=[]
    #     self.store[key].append((value,timestamp))


    # def get(self, key: str, timestamp: int) -> str:
    #     if key not in self.store:
    #         return ""
    #     values=self.store[key]
    #     best_time=-1
    #     value=''
    #     for val in values:
    #         if val[1]<=timestamp and val[1]>best_time:
    #             best_time=val[1]
    #             value=val[0]
    #     return value

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append((value,timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        low=0
        high=len(self.store[key])-1
        values=self.store[key]
        current=''
        while low<=high:
            mid=(low+high)//2
            value=values[mid][1]
            if value<=timestamp:
                current=values[mid][0]
                low=mid+1
            else:
                high=mid-1
        return current
            
            



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)