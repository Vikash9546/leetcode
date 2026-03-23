class Solution:
    def mySqrt(self, x: int) -> int:
        a=0
        if x==0:
            return 0
        if x==1:
            return 1
        if x==2:
            return 1
        for i in range(1,x):
            a=i*i

            if a==x:
                return i
            elif a>x:
                return i-1

        
        