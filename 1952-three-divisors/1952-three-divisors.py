class Solution:
    def isThree(self, n: int) -> bool:
        # root = int(n**0.5)
        # if root*root!=n:
        #     return False
        # for i in range(2,root):
        #     if root%i==0:
        #         return False
        # return root>1

        if n==1 and n==2:
            return False
        res=[1,n]
        for i in range(2,n):
            if n%i==0:
                res.append(i)
        return len(res)==3