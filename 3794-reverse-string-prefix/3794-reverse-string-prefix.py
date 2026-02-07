class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        l=list(s)
        i=0
        j=k-1
        # print(l)
        while i<j:
            a=l[i]
            b=l[j]
            l[i]=b
            l[j]=a
            i+=1
            j-=1
        c=''.join(l)
        return c
        