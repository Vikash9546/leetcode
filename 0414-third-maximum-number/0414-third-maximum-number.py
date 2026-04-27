class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=set(nums)
        l=list(s)
        l.sort(reverse=True)
        if len(l)<3:
            return max(l)
        return l[2]
        
        