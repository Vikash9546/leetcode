class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        import math
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                f=str(nums[i])
                l=str(nums[j])
                if math.gcd(int(f[0]),int(l[len(l)-1]))==1:
                    c+=1
        return c
        