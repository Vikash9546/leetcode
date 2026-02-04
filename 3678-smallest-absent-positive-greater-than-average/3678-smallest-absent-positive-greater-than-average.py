class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        n=len(nums)
        s=sum(nums)
        avg=int(s/n)
        t=avg+1
        for i in nums:
            if t in nums:
                t+=1
        p=1
        if t<=0:
            for i in nums:
                if p in nums:
                    p+=1
            return p
        return t

        
            

        

        