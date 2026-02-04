class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        res=[]
        d={}
        for i in nums:
            for j in i:
                if j in d:
                    d[j]+=1
                    if d[j]==n:
                        res.append(j)
                else:
                    d[j]=1
                    if d[j]==n:
                        res.append(j)
        res.sort()
        if len(res)==0:
            return []
        return res
            
        