class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # boats=0
        # used=[False]*len(people)
        # for i in range(len(people)):
        #     if used[i] is True:
        #         continue
        #     boats+=1
        #     used[i]=True
        #     for j in range(i+1, len(people)):
        #         if not used[j] and people[i]+people[j]<=limit:
        #             used[j]=True
        #         break

        # return boats
        people.sort()  
        l, r=0, len(people)-1
        boats=0
        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1
                r-=1
                boats+=1
            else:
                r-=1
                boats+=1
        return boats
