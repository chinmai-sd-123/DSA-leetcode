class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #we cannot buy on day 2 and sell on day 1
        # we should maintain max_profit
        # no same day
        # if no transcations return 0
        # max_profit=0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit=prices[j]-prices[i]
        #         max_profit= max(max_profit, profit)
        # return max_profit

        #optmimal approach:
        l=0
        max_profit=0
        for r in range(l,len(prices)):
            if prices[l]>prices[r]:
                l=r
            else:
                profit=prices[r]-prices[l]
                max_profit=max(max_profit, profit)
        return max_profit