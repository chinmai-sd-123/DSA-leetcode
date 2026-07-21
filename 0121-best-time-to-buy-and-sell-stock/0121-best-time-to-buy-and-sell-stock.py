class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

    # brute force solution- o(n^2)- space -O(n)
        # profit=0
        # for i in range(len(prices)):
        #     current_profit=0
        #     for j in range(i+1,len(prices)):
        #         if prices[j]-prices[i]>current_profit:
        #             current_profit=prices[j]-prices[i]
        #         profit=max(profit,current_profit)
        
        # return profit

    # sliding window time - o(n) and space- O(1)


        l=0
        profit=0
        for r in range(len(prices)):
            if prices[l]>prices[r]:
                l=r
            else:
                profit=max(profit, prices[r]-prices[l])
        return profit
