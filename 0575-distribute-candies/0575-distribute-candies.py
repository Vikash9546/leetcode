class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        d={}
        for i in candyType:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        k=d.keys()
        if len(k)>len(candyType)//2:
            return len(candyType)//2
        else:
            return len(k)


        