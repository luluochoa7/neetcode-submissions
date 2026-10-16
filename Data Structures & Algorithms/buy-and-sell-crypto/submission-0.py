class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            # Is it profitable?
            if prices[left] < prices[right]:
                # Get profit
                profit = prices[right] - prices[left]
                # Update maxProfit
                maxProfit = max(maxProfit, profit)
            # Not profitable
            else:
                # Move left to be right
                left = right
            # Move right regardless one to see the next sell possibility
            right += 1
        # Return maxProfit
        return maxProfit
