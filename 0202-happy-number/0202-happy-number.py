class Solution:
    def isHappy(self, n: int) -> bool:
        def get(n):
            res=0
            while n:
                d=n%10
                res+=d**2
                n=n//10
            return res

        slow=get(n)
        fast=get(get(n))
        while slow!=fast:
            if fast==1:
                return True
            slow=get(slow)
            fast=get(get(fast))
        if slow==1:
            return True
        else:
            return False


        