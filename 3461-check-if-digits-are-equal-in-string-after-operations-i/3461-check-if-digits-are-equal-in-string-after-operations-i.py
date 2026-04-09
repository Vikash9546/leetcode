class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def check(s):
            i=0
            j=1
            res=''
            while j<len(s):
                a=int(s[i])
                b=int(s[j])
                res+=str((a+b)%10)
                i+=1
                j+=1
            return res
        result=check(s)
        while len(result)>2:
            result=check(result)
        return result[0]==result[1]
            


        