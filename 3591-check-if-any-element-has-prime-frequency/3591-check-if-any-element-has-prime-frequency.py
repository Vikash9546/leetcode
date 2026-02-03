class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        n=len(nums)
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        v=d.values()
        # print(v) 
        p=[1]*(n+1)
        p[0]=p[1]=0
        for i in range(2,n+1):
            if p[i]:
                for j in range(i*i,n+1,i):

                    p[j]=0
        for i in v:
            if p[i]==1:
                return True
        return False
            
        
                    
                        
        