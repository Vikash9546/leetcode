class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        res=dict(sorted(d.items(), key=lambda item: item[1],reverse=True))

        s=''
        for i,v in res.items():
            
            s+=i*d[i]
        return s

        