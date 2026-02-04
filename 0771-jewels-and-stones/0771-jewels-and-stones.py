class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d={}
        for i in stones:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        for i in jewels:
            if i in d:
                c+=d[i]
        return c

        