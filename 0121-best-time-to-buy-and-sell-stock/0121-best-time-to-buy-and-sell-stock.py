class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices=[]
        # max_p=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         p=prices[j]-prices[i]
        #         max_p=max(p,max_p)
        # return max_p
        
        min_p=float('inf')
        max_p=0
        for i in range(len(prices)):
            if prices[i]<min_p:
                min_p= prices[i]
            else:
                p=prices[i]-min_p
                max_p=max(max_p,p)

        return max_p