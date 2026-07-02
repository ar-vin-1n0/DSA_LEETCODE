class Solution(object):
    def maxProfit(self, prices):
        min_p = prices[0]
        max_p = 0

        for p in prices:
            if p < min_p:
                min_p = p
            profit = p - min_p
            if profit > max_p:
                max_p = profit
        return max_p   