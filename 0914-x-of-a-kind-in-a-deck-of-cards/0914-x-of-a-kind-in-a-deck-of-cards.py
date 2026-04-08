class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        import math
        d={}
        for i in deck:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        v=list(d.values())
        res=v[0]
        for i in range(1,len(v)):
            res=math.gcd(res,v[i])
        return res>1
         
        
        

        




        