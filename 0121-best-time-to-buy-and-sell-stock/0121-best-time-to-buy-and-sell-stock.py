class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p=0
        min_p=float('inf')
        for i in range(len(prices)):
            if prices[i]<min_p:
                min_p=prices[i]
            else:
                p=prices[i]-min_p
                max_p=max(max_p,p)
        return max_p