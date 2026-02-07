class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        n=len(s)
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in range(n):
            if d[s[i]]==1:
                return i
        return -1
        
        