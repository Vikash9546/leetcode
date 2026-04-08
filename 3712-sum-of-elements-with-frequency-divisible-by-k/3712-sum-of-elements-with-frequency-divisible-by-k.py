class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s=0
        for i,v in d.items():
            if v%k==0:
                s+=i*v
        return s
        