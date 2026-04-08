class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        # d=0
        # p=[0]*len(hours)
        # p[0]=hours[0]
        # for i in range(1,len(hours)):
        #     p[i]=p[i-1]+hours[i]
        # for i in p:
        #     if i%24==0:
        #         d+=1
        # return d
        d={}
        for i in hours:
            i=i%24
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        for i in hours:
            i=i%24
            d[i]-=1
            a=24-i
            a=a%24
            if  a in d and d[a]>0:
                c+=d[a]
            
        return c