class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(capacity):
            n_d=1
            curr_s=0
            for i in weights:
                if curr_s+i>capacity:
                    n_d+=1
                    curr_s=0
                curr_s+=i
            return n_d<=days
        left=max(weights)
        right=sum(weights)
        while left<right:
            mid=(left+right)//2
            if helper(mid):
                right=mid
            else:
                left=mid+1
        return left