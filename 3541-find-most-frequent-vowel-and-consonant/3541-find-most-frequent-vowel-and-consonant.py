class Solution:
    def maxFreqSum(self, s: str) -> int:
        d={}
        for i in s:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
        e={}
        for i in s:
            if i!='a' and i!='e' and i!='i' and i!='o' and i!='u':
                if i in e:
                    e[i]+=1
                else:
                    e[i]=1
        a=b=0
        if len(d.values())!=0:
            a=max(d.values())
        if len(e.values())!=0:
            b=max(e.values())
        return a+b
                
        