class Solution:
    def digitCount(self, num: str) -> bool:
        d={}
        for i in range(len(num)):
            d[str(i)]=0
        for i in num:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        # print(d)
        for j in range(len(num)):
            if num[j]==str(d[str(j)]):
                continue
            else:
                return False
        return True

        